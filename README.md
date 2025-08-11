# pg-vectorstore-boilerplate
Minimal setup for a postgres-hosted vectorstore using `pgvector`, `sqlalchemy` and `alembic`.  
This repository was created to help `langchain-postgres`'s maintainers reproduce the error raised by [this issue](https://github.com/langchain-ai/langchain-postgres/issues/241).

## Initial requirements
  - OS : Ubuntu >=20.04 LTS
  - Python ~=3.12.10
  - Docker installed

## Installation

Using uv :
```bash
uv sync
```

With poetry :
```bash
poetry install
```
Or pip :
```bash
pip install -r requirements.txt
```

## Run the project

1. Configure database settings in a .env file at project's root level (see provided template.env)
```bash
# .env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=vectorstore_db
POSTGRES_SCHEMA=public
POSTGRES_SYNC_PREFIX=postgresql
POSTGRES_ASYNC_PREFIX=postgresql+asyncpg
VECTOR_DIMS=768
```

3. At project's root level, run :
```bash
alembic upgrade head
```

4.  Verify that tables have been successfully created

5. In your favortie SQL editor, run the following query :
```sql
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'vectorstore' AND table_schema = 'public';
```
The column `embedding` should be of type `USER-DEFINED` or `vector`.
