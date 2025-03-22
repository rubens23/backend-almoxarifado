from decimal import Decimal
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, Numeric
from pydantic import BaseModel



Base = declarative_base()

#Definição das colunas da tabela de Pagamentos
class Pagamento(Base):
    __tablename__ = "pagamentos"

    id= Column(Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    metodo_pagamento = Column(String, nullable=False)
    criado_em = Column(DateTime, nullable=False)

    # Relacionamentos para acessar os dados do Pedido e Usuario
    pedido = relationship("Pedido", backref="pagamentos")
    usuario = relationship("Usuario", backref="pagamentos")


# classe que lida melhor com as respostas da requisição http
class PagamentoCreate(BaseModel):
    id_pedido: int
    id_usuario: int
    valor: Decimal
    metodo_pagamento: str
    criado_em: DateTime

    class Config:
        orm_mode = True









