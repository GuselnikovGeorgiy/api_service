from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.storage.router import router as storage_router


def create_app() -> FastAPI:
    app = FastAPI(
        root_path="/api",
        title="Storage Service",
        description="This service stores and processes data",
        debug=True,
    )

    app.include_router(storage_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
