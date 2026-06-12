# version

- `python3 --version`
  Python 3.13.2
- `docker --version`
  Docker version 28.0.4, build b8034c0
- `docker compose version`
  Docker Compose version v2.34.0-desktop.1
- `git --version`
  git version 2.39.5 (Apple Git-154)
- `uv --version`
  uv 0.11.21

# folder structure

- uv
  `curl -LsSf https://astral.sh/uv/install.sh | sh`

- folder creation
  `mkdir -p backend/app/api/v1 backend/app/core backend/app/db/models backend/app/db/repositories backend/app/service backend/app/rag/graph/nodes backend/app/rag/chunkers backend/app/rag/embedders backend/app/rag/retrievers backend/app/tasks backend/app/schema backend/alembic/versions backend/tests/unit backend/postgres docker/postgres docker/postgres docker/qdrant scripts`

- init file creation
  `touch backend/app/**init**.py backend/app/api/**init**.py backend/app/api/v1/**init**.py backend/app/core/**init**.py backend/app/db/**init**.py backend/app/db/models/**init**.py backend/app/db/repositories/**init**.py backend/app/rag/**init**.py backend/app/rag/chunkers/**init**.py backend/app/rag/embedders/**init**.py backend/app/rag/graph/**inti**.py backend/app/rag/graph/nodes/**init**.py backend/app/rag/retrievers/**init**.py backend/app/schema/**init**.py backend/app/service/**init**.py ./backend/app/tasks/**init**.py ./backend/tests/**init**.py ./backend/tests/unit/**init**.py ./backend/tests/integration/**init**.py`

- config file creation
  `touch .env.example .env.development docker-compose.yml Makefile .pre-commit-config.yaml`

- backend file creation
  `touch backend/pyproject.toml backend/alembic.ini backend/Dockerfile.dev`

# file creation
- pyproject.toml: create and basic code

# installation
- `uv add fastapi 'uvicorn[standard]' pydantic-settings structlog orjson`
    - fastapi: web framework
    - uvicorn[standard]: the ASGI server that runs fastapi server
    - pydantic-settings: manages app's configuration from environment variables or .env files 
    - structlog: it outputs logs as structured data in form of JSON
    - orjson: a replacement for python's built in json

- `uv add --dev ruff pytest pytest-asyncio httpx`
    - ruff: python linter and formatter
        - `ruff check .`: check for lint errors
        -  `ruff format .`: format code 
    - pytest: python testing framework
        - `pytest`: runs all test
        -  `pytest tests/`: runs tests in specific folder
    - pytest-asyncio: lets pytest run async test functions
    - httpx: modern http client used to test FastAPI endpoint   

- 