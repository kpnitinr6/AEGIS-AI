"""
AEGIS AI API Routes

This module contains all public API endpoints.
"""

from fastapi import APIRouter

from backend.core.logger import logger
from backend.core.settings import settings

router = APIRouter()


@router.get("/")
def home():
    logger.info("Home endpoint accessed")

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@router.get("/health")
def health():
    logger.info("Health endpoint accessed")

    return {
        "status": "healthy",
    }


@router.get("/version")
def version():
    logger.info("Version endpoint accessed")

    return {
        "version": settings.APP_VERSION,
    }


@router.get("/about")
def about():
    logger.info("About endpoint accessed")

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "description": settings.APP_DESCRIPTION,
    }