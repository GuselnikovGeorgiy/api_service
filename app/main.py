import uvicorn
from fastapi import FastAPI

from app.storage.router import router as storage_router


app = FastAPI(
    root_path="/api",
    title="Store service",
    description="This service stores and processes data",
    debug=True,
)

app.include_router(storage_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)