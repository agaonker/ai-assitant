# AI-Powered Personal Assistant

An intelligent personal assistant built with Python, Pydantic, and GPT-2 running locally. This assistant can help automate tasks, manage schedules, and provide intelligent responses to user queries.

## Features

- Task automation and management
- Natural language processing using local GPT-2 model
- Schedule management
- Intelligent response generation
- Extensible architecture
- No API keys required - runs completely offline

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

1. Start the assistant:
   ```bash
   python src/ai_assistant/main.py
   ```

2. The assistant will be available at `http://localhost:8000`
3. Open `http://localhost:8000/docs` for interactive API documentation

## Model Information

This project uses GPT-2 which runs completely locally on your machine:
- No API keys required
- First run will download the model (~500MB)
- Model is cached locally for subsequent runs
- Runs on CPU, no GPU required

## Project Structure

- `main.py`: Main application entry point
- `models.py`: Pydantic models for data validation
- `config.py`: Configuration settings
- `requirements.txt`: Project dependencies

## Git Instructions

Before pushing, you should create a `.gitignore` file to avoid pushing unnecessary files. Here are the commands to initialize and push your code:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AI Assistant with GPT-2"

# Add the remote repository
git remote add origin https://github.com/agaonker/ai-assitant.git

# Push to main branch
git push -u origin main
```

Important: Your `.env` file contains an OpenAI API key. You should:
1. Remove the API key from the `.env` file before pushing
2. Add `.env` to your `.gitignore` (already included in the above)
3. Create a `.env.example` file without the actual key:

```bash
cat > .env.example << EOL
MODEL_NAME=gpt2
MAX_TOKENS=1000
TEMPERATURE=0.7
EOL
```

echo "__pycache__/
*.py[cod]
*$py.class
.Python
.env
.venv/
venv/
ENV/
.cache/
.vscode/
.idea/
.DS_Store" > .gitignore
```

echo '[project]
name = "ai-assistant"
version = "0.1.0"
description = "AI-Powered Personal Assistant for Task Automation"
authors = ["Ashish Gaonker <ashish.gec@gmail.com>"]
dependencies = [
    "pydantic>=2.0.0",
    "pydantic-settings>=2.0.0",
    "python-dotenv>=1.0.0",
    "fastapi>=0.100.0",
    "uvicorn>=0.23.0",
    "python-multipart>=0.0.6",
    "transformers>=4.30.0",
    "torch>=2.0.0",
    "numpy>=1.24.0",
    "scikit-learn>=1.0.0"
]
requires-python = ">=3.9"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/ai_assistant"]

[tool.ruff]
line-length = 88
target-version = "py39"

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
]' > pyproject.toml