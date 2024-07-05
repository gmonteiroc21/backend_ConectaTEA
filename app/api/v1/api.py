from fastapi import APIRouter
from app.api.v1.routes.usuario import router as usuario
api_router = APIRouter()

api_router.include_router(usuario, prefix="/usuarios", tags=["usuarios"])