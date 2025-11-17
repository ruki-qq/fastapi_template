# FastAPI Template

This is a FastAPI template with async SQLAlchemy, Alembic migrations, PostgreSQL, and Docker support

Using **Poetry** as dependency management

## Includes

- **FastAPI** - Web framework for building APIs
- **Async SQLAlchemy** - Asynchronous db operations ORM
- **Alembic** - Database migrations, initializes with <ins>-t async</ins>
- **PostgreSQL** - Relational database
- **Docker** - Containerize application with docker-compose
- **Pytest** - Testing setup with async support
- **CORS Middleware** - Pre-configured for cross-origin requests
- **Logging** - Logging configuration

## Tech Stack

- Python 3.13
- FastAPI 0.121+
- SQLAlchemy 2.0+
- PostgreSQL 16
- Alembic 1.17+
- Pydantic Settings
- Docker & Docker Compose

## Project Structure

```
.
├── src/
│   ├── main.py                 # Application entry point
│   ├── app/
│   │   ├── app.py             # FastAPI app initialization
│   │   ├── routers/           # API route handlers
│   │   │   └── api/           # API routes
│   │   ├── services/          # Business logic layer
│   │   └── schemas/           # Pydantic models
│   └── core/
│       ├── config.py          # Application settings
│       ├── db_helper.py       # Database session management
│       ├── logger.py          # Logging configuration
│       └── models/            # SQLAlchemy models
│           └── base.py        # Base model class
├── alembic/                   # Database migrations
├── tests/                     # Tests
│   ├── conftest.py           # Pytest fixtures
│   └── utils.py              # Test utilities
├── docker-compose.yml        # Docker services definition
├── Dockerfile               # Application container
├── pyproject.toml          # Project dependencies
└── alembic.ini            # Alembic configuration
```

## Prerequisites

- Python 3.13+
- Poetry
- Docker and Docker Compose

## Installation

### Using Poetry (Local Development)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd fastapi_template
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Activate virtual environment**
   ```bash
   poetry shell
   ```

### Using Docker

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd fastapi_template
   ```

2. **Build and start containers**
   ```bash
   docker-compose up --build
   ```

## Configuration

### Environment Variables

The application uses the following environment variables (defined in `docker-compose.yml` or `.env`):

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_HOST` | Database host | `127.0.0.1` |
| `DB_PORT` | Database port | `5432` |
| `DB_USER` | Database user | `postgres` |
| `DB_PASSWORD` | Database password | `postgres` |
| `DB_NAME` | Database name | `db_dev` |
| `DB_URL` | Full database URL (auto-generated) | - |

### Database Settings

Edit `src/core/config.py` to customize database settings:

```python
class DBSettings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "db_dev"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 5432
    echo: bool = True  # Set to False in production
```

## Running the Application

### Local Development

```bash
poetry run python src/main.py
```

The application will start at `http://localhost:8000`.

### With Docker

```bash
docker-compose up
```

The application will be available at `http://localhost:8000`.

## Database Migrations

### Create a new migration

```bash
alembic revision --autogenerate -m "description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migration

```bash
alembic downgrade -1
```

## Testing

### Run all tests

```bash
poetry run pytest -vvv
```

### Run with coverage

```bash
poetry run pytest --cov=src --cov-report=html
```

### Run specific test file

```bash
poetry run pytest tests/test_example.py
```

The test suite uses:
- **SQLite in-memory database**
- **Async pytest fixtures** with proper session management
- **Dependency overrides** for database session injection

## API Documentation

Once the application is running, visit:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

## Development

### Code Formatting

This template uses Black with a 120-character line length:

```bash
poetry run black src tests
```

### Linting

```bash
poetry run flake8 src tests
```

### Adding New Routes

1. Create router in `src/app/routers/api/`
2. Import and include in `src/app/routers/api/__init__.py`
3. Routes will be automatically prefixed with `/api`

Example:

```python
# src/app/routers/api/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def list_users():
    return {"users": []}
```

### Adding New Models

1. Create model in `src/core/models/`
2. Import in `src/core/models/__init__.py`
3. Generate migration: `alembic revision --autogenerate -m "add user model"`
4. Apply migration: `alembic upgrade head`

Example:

```python
# src/core/models/user.py
from sqlalchemy.orm import Mapped, mapped_column
from core.models.base import Base

class User(Base):
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True)
```

## Docker Services

### PostgreSQL Database

- **Image**: postgres:16
- **Port**: 5432
- **Credentials**: qa_user/qa_password
- **Database**: qa
- **Volume**: pgdata (persistent storage)

### Application

- **Port**: 8000
- **Auto-reload**: Enabled via volume mount (`./src:/app/src`)

### Useful Docker Commands

```bash
# View logs
docker-compose logs -f app

# Restart services
docker-compose restart

# Stop services
docker-compose down

# Remove volumes (deletes database)
docker-compose down -v

# Run migrations in container
docker-compose exec app alembic upgrade head
```

## Project Conventions

### Code Organization

- **Routers**: Handle HTTP requests/responses, input validation
- **Services**: Business logic, database operations
- **Schemas**: Pydantic models for request/response validation
- **Models**: SQLAlchemy ORM models
