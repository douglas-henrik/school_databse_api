from fastapi import FastAPI, Depends, HTTPException # Importando FastAPI, depends e excption http
from sqlalchemy.orm import Session # Importando Session
from sqlalchemy.orm import joinedload # Impotando joinedload
import models, schemas # Importa o models e os schemas
from database import engine, SessionLocal # Importa nosso engine e session local
from typing import List # Importando type lista

models.Base.metadata.create_all(bind=engine) # Criando DataBase

app = FastAPI() # Criando API

def get_db(): # Função para abrir DataBase e Fechar
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota POST para criar estudantes
@app.post('/estudantes', response_model=schemas.Estudante)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session=Depends(get_db)): # Função de criar estudantes, estudante é validado pela schema e database chama o get_db
    db_estudante = models.Estudante( # Criando instacia de Estudante
        nome = estudante.nome, # Desempacota o nome
        email = estudante.email, # Desempacota o email
        perfil = models.Perfil( # Cria uma instancia do Perfil
            idade = estudante.perfil.idade, # Desempacota a idade
            endereco = estudante.perfil.endereco # Desempacota o endereço
        )
    )
    db.add(db_estudante) # Prepara pra adicionar ao DataBase
    db.commit() # Envia alterações
    db.refresh(db_estudante) # Atualiza os dados autoomaticos, como os ID
    return db_estudante # Retorna o estudante

# Rota GET para buscar todos os estudantes em uma lista
@app.get('/estudantes', response_model=List[schemas.Estudante])
def listar_estudantes(db: Session=Depends(get_db)): # Recebe sessão do DataBase como parametro
    estudantes = db.query(models.Estudante).all() # Buscar tudo que se encontra na tabela estudantes
    return estudantes # Retornar a lista com todos os estudantes

# Rota GET para buscar um estudante
@app.get('/estudantes/', response_model=schemas.Estudante)
def consultar_estudante(nome_estudante: str, db: Session=Depends(get_db)): # Busca um unico estudante pelo nome
    estudante = db.query(models.Estudante).filter(models.Estudante.nome == nome_estudante).first() # Retorna o primeiro estudante cujo nome seja igual ao solicitado
    return estudante

# Rota DELETE para deletar estudantes
@app.delete('/estudantes/', response_model=schemas.Estudante)
def deletar_estudante(id_estudante: int, db: Session=Depends(get_db)): # Busca o estudante pelo ID
    estudante = db.query(models.Estudante).filter(models.Estudante.id == id_estudante).first() # Retorna o primeiro estudante cujo ID seja igual o solicitado
    db.delete(estudante) # Deleta estudante do DataBase
    db.commit() # Confirma as alterações
    return estudante # Retorna o estudante removido