from decimal import Decimal
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, ForeignKey, Numeric
from pydantic import BaseModel

Base = declarative_base()

# Tabela que representa os produtos que vão
# dentro do pedido
class ItensPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    id_produto = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    quantidade = Column(Integer, nullable=False, default=1)
    preco_unitario = Column(Numeric(10, 2), nullable=False)

    produto = relationship("Produto", backref="itens_pedido")  # Relacionamento com a tabela Produto
    pedido = relationship("Pedido", backref="itens")  # Relacionamento com a tabela Pedido


class ItensPedido(BaseModel):
    id_pedido: int
    id_produto: int
    quantidade: int
    preco_unitario: Decimal

    class Config:
        orm_mode = True