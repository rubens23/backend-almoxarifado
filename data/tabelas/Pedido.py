from decimal import Decimal
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, Numeric
from pydantic import BaseModel



Base = declarative_base()

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    endereco = Column(String, nullable=False)
    status_pedido = Column(String, nullable=False)
    criado_em = Column(DateTime, nullable=False)
    atualizado_em = Column(DateTime, nullable=True)

    # relacionamentos para acessar os dados dos usuarios e os itens do 
    # pedido
    usuario = relationship("Usuario", backref="pedidos")
    itens = relationship("ItensPedido", backref="pedido")


# classe que lida melhor com as respostas da requisição http
class PedidoCreate(BaseModel):
    id_usuario: int
    valor_total: Decimal
    endereco: str
    status_pedido: str
    criado_em: DateTime
    atualizado_em: DateTime

    class Config:
        orm_mode = True




