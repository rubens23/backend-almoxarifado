from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, Integer, String
from pydantic import BaseModel

Base = declarative_base()


# Tabela que representa os Usuários
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    endereco = Column(String, nullable=False)
    criado_em = Column(DateTime, nullable=False)

class UsuarioCreate(BaseModel):
    id: int
    nome: str
    email: str
    endereco: str
    criado_em: DateTime

    class Config:
        orm_mode = True
