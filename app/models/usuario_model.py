from sqlalchemy import Boolean, Column, Integer, String

from app.core.config.config import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    username = Column(String(256), index=True, nullable=False, unique=True)
    email = Column(String(256), index=True, nullable=False, unique=False)
    senha = Column(String(256), nullable=False)
    eh_admin = Column(Boolean, default=False)
