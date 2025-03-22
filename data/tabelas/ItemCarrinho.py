from decimal import Decimal
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, ForeignKey, Numeric
from pydantic import BaseModel

Base = declarative_base()


# tabela que representa os produtos que vão
# dentro do carrinho
class ItemCarrinho(Base):
    __tablename__ = "itens_carrinho"

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_produto = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)

    # Relacionamento com o produto
    produto = relationship("Produto", backref="itens_carrinho")

    # Relacionamento com o carrinho
    carrinho = relationship("Carrinho", backref="itens_carrinho")

class ItemCarrinhoCreate(BaseModel):
    id_usuario: int
    id_produto: int
    quantidade: int
    preco: Decimal

    class Config:
        orm_mode = True