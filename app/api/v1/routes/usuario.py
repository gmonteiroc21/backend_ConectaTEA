from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi import status as http_status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.usuario_model import UsuarioModel
from app.core.deps.dependencies import get_session


router = APIRouter()

@router.get("/", status_code=http_status.HTTP_200_OK)
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    usuarios_db = await db.execute(select(UsuarioModel))
    usuarios_db = usuarios_db.scalars().all()
    return usuarios_db

@router.get("/{usuario_id}", status_code=http_status.HTTP_200_OK)
async def get_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    usuario_db = await db.execute(select(UsuarioModel).where(UsuarioModel.id == usuario_id))
    usuario_db = usuario_db.scalars().first()
    return usuario_db

@router.post("/", status_code=http_status.HTTP_201_CREATED)
async def create_usuario(user_info: dict, db: AsyncSession = Depends(get_session)):
    usuario = UsuarioModel(**user_info)
    db.add(usuario)
    await db.commit()
    return usuario.id