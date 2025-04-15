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
   source .venv/bin/activate 
   ```

3. Install uv (faster package installer):
   ```bash
   pip install uv
   ```

4. Install dependencies using uv:
   ```bash
   uv pip install -e .
   ```

   Note: All dependencies are managed in pyproject.toml for better reproducibility.

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

## Development

Dependencies are managed through `pyproject.toml` using modern Python packaging standards:
- Uses `uv` for faster package installation
- Includes development tools configuration (ruff, etc.)
- Specifies exact version requirements for reproducibility
