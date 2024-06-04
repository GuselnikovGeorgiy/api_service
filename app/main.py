from fastapi import FastAPI

from app.storage.router import router as storage_router


app = FastAPI(
    docs_url="/api/docs",
    root_path="/api",
    title="Store service",
    description="This service stores and processes data",
    debug=True,
)

app.include_router(storage_router)
