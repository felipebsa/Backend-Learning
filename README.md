# Backend Learning

A personal repository to document my backend development journey, focusing on Python and FastAPI.

## How to run

**1. Install dependencies:**
```bash
pip install -r requirements.txt
```

**2. Navigate to the folder you want to run:**
```bash
cd lecture-06
```

**3. Start the server:**
```bash
python -m uvicorn main:app --reload
```

**4. Open in browser:**
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs

## Progress

### FastAPI
| Lecture | Topics |
|---------|--------|
| lecture-01 | Endpoints, Pydantic, HTTP Errors |
| lecture-02 | SQLAlchemy, SQLite |
| lecture-03 | SQLAlchemy + FastAPI - Full CRUD, project structure (models, schemas, routes) |
| lecture-04 | Frontend integration, CORS, HTML/CSS/JS |
| lecture-05 | SQLAlchemy 2.0 - Mapped, mapped_column, DeclarativeBase, Full CRUD |
| lecture-06 | SQLAlchemy 2.0 - Modern queries with select, execute, scalars + Depends injection |

### Tools
| Folder | Topics |
|--------|--------|
| tools/alembic-train | Alembic - migrations (revision, autogenerate, upgrade/downgrade), env.py configuration, versioning schema without losing data |
| tools/pytest-train | Pytest - fixtures, TestClient, dependency overrides, isolated test database, response_model with `from_attributes` |

## Stack

- [Python](https://python.org)
- [FastAPI](https://fastapi.tiangolo.com)
- [Pydantic](https://docs.pydantic.dev)
- [Uvicorn](https://www.uvicorn.org)
- [SQLAlchemy](https://sqlalchemy.org)
- [Alembic](https://alembic.sqlalchemy.org)
- [Pytest](https://docs.pytest.org)