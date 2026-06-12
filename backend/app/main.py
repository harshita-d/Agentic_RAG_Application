from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager 
import structlog 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging

logger=structlog.get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI)->AsyncGenerator[None, None]:
    configure_logging()
    logger.info("starting", app=settings.app_name, env=settings.environment)
    yield
    logger.info("shutdown complete")

def create_app()->FastAPI:
    app=FastAPI(
        title=settings.app_name,
        docs_url="/docs" if settings.is_development else None,
        lifespan=lifespan
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:3000'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    register_exception_handlers(app)

    @app.get("/health")
    async def health()-> dict:
        return {"status":"ok", "app":settings.app_name}
    
    return app

app=create_app()