from fastapi import APIRouter

from .models import router

models_router = APIRouter()
models_router.include_router(router, tags=["model模块"])

__all__ = ["models_router"]
