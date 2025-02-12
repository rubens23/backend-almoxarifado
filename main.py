from sqlalchemy.orm import Session
from database import engine, get_db
from modelo import Base, Produto, ProdutoCreate
from fastapi import FastAPI, Depends, HTTPException



#Cria as tabelas no BD ( se não existirem :) )
def create_tables():
    Base.metadata.create_all(bind=engine)

#Chama o FASTAPI para depois ser usado para criar a rota
app = FastAPI()


create_tables()




@app.post("/produtos/", response_model=ProdutoCreate)
async def criar_produto(
        #aqui colocamos os parâmetros que queremos quando a função for executada 
        produto: ProdutoCreate,
        db: Session = Depends(get_db) 
 
):
    try:
        novo_produto = Produto(
            nome=produto.nome, data_vencimento=produto.data_vencimento , quantidade= produto.quantidade , categoria=produto.categoria
            #aqui são parâmetros para que a variavel (novo produto) leve a informação até a classe Produto que esta em modelo.py
        )    
        db.add(novo_produto) #executa a função e add novo produto..
        db.commit() #salva as alterações 
        db.refresh(novo_produto) #atualiza os dados do novo (novo produto) 
        return novo_produto
    except Exception as e:
        db.rollback() #se der erro, desfaz a transação para evitar inconsistências
        raise HTTPException(status_code=500, detail=f"Erro ao criar produto: {str(e)}")

        