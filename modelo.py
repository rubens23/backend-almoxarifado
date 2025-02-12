from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from datetime import date
from typing import Optional



#Cria a Base para a classe, isso se resume a construção da tabela :) 
Base = declarative_base()


#Definição das colunas da tabela de Produtos
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer,primary_key=True, index=True )
    nome = Column(String, index=True, nullable=False   )
    data_vencimento = Column(Date)
    quantidade = Column(Integer, default=1)
    categoria = Column (String, nullable=False )


# classe que lida melhor com as respostas da requisição http
class ProdutoCreate(BaseModel):
    nome: str
    data_vencimento: date
    quantidade: int = 1
    categoria: Optional[str] = None

    class Config:
        orm_mode = True