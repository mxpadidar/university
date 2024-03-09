from fastapi import FastAPI

from backbone.adapters.postgres import create_schemas, create_tables
from university.entrypoints.routes import router as university_router

create_schemas()
create_tables()

app = FastAPI()

app.include_router(university_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
