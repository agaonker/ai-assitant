from fastapi import FastAPI, HTTPException
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch
from typing import List
import uvicorn
from datetime import datetime

from models import Task, UserQuery, AssistantResponse, Schedule, TaskUpdate
from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Initialize the language model
model_name = settings.MODEL_NAME
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# In-memory storage (replace with database in production)
tasks = []
schedules = []

@app.post(f"{settings.API_V1_STR}/tasks/", response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.get(f"{settings.API_V1_STR}/tasks/", response_model=List[Task])
async def get_tasks():
    return tasks

@app.put(f"{settings.API_V1_STR}/tasks/{{task_id}}", response_model=Task)
async def update_task(task_id: str, task_update: TaskUpdate):
    for task in tasks:
        if task.id == task_id:
            for field, value in task_update.dict(exclude_unset=True).items():
                setattr(task, field, value)
            task.updated_at = datetime.now()
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post(f"{settings.API_V1_STR}/query/", response_model=AssistantResponse)
async def process_query(query: UserQuery):
    # Generate response using the language model
    response = text_generator(
        query.query,
        max_length=settings.MAX_TOKENS,
        temperature=settings.TEMPERATURE,
        num_return_sequences=1
    )[0]['generated_text']
    
    # Simple action suggestion based on keywords
    suggested_actions = []
    if "schedule" in query.query.lower():
        suggested_actions.append("Would you like me to create a new schedule?")
    if "task" in query.query.lower():
        suggested_actions.append("Would you like me to create a new task?")
    
    return AssistantResponse(
        response=response,
        suggested_actions=suggested_actions,
        confidence=0.8
    )

@app.post(f"{settings.API_V1_STR}/schedules/", response_model=Schedule)
async def create_schedule(schedule: Schedule):
    schedules.append(schedule)
    return schedule

@app.get(f"{settings.API_V1_STR}/schedules/", response_model=List[Schedule])
async def get_schedules():
    return schedules

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    ) 