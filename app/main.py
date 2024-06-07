from fastapi import FastAPI

from app.storage.router import router as storage_router


def create_app() -> FastAPI:
    app = FastAPI(
        root_path="/api",
        title="Storage Service",
        description="This service stores and processes data",
        debug=True,
    )

    app.include_router(storage_router)

    return app
