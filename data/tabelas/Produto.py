from decimal import Decimal
from xmlrpc.client import DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, Numeric
from pydantic import BaseModel
from datetime import date
from typing import Optional

Base = declarative_base()

#Definição das colunas da tabela de Produtos
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer,primary_key=True)
    nome = Column(String, index=True, nullable=False)
    descricao = Column(String)
    criado_em = Column(DateTime, index = True, nullable=False)
    categoria = Column (String, nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)
    qnt_estoque = Column(Integer, nullable=False, default= 0)



# classe que lida melhor com as respostas da requisição http
class ProdutoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    criado_em: DateTime
    quantidade: int = 1
    categoria: str
    preco: Decimal
    qnt_estoque: int

    class Config:
        orm_mode = True

