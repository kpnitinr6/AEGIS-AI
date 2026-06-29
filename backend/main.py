"""
AEGIS AI

Main application entry point.
"""

from fastapi import FastAPI

from backend.api.routes import router
from backend.core.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)

app.include_router(router)