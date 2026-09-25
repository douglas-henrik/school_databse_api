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
    if estudante.perfil.idade <= 0: # Valida a idade do estudante
        raise HTTPException(status_code=422, detail='Idade inválida') # Lança exceção se estiver incorreto
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
    if not estudantes: # Verifica se há estudantes
        raise HTTPException(status_code=404, detail='Nenhum estudante cadastrado') # Lança a exceção
    return estudantes # Retornar a lista com todos os estudantes

# Rota GET para buscar um estudante
@app.get('/estudantes/', response_model=schemas.Estudante)
def consultar_estudante(nome_estudante: str, db: Session=Depends(get_db)): # Busca um unico estudante pelo nome
    estudante = db.query(models.Estudante).filter(models.Estudante.nome == nome_estudante).first() # Retorna o primeiro estudante cujo nome seja igual ao solicitado
    if not estudante: # Verifica se existe esse estudante
        raise HTTPException(status_code=404, detail=f'Nenhum {nome_estudante} encontrado') # Lança a exceção
    return estudante

# Rota DELETE para deletar estudantes
@app.delete('/estudantes/', response_model=schemas.Estudante)
def deletar_estudante(id_estudante: int, db: Session=Depends(get_db)): # Busca o estudante pelo ID
    estudante = db.query(models.Estudante).filter(models.Estudante.id == id_estudante).first() # Retorna o primeiro estudante cujo ID seja igual o solicitado
    if not estudante: # Verifica se existe esse estudante
        raise HTTPException(status_code=404, detail='Nenhum estudante com esse ID encontrado') # Lança a exceção
    db.delete(estudante) # Deleta estudante do DataBase
    db.commit() # Confirma as alterações
    return estudante # Retorna o estudante removido

# Rota POST para criar professores
@app.post('/professores', response_model=schemas.Professor)
def criar_professor(professor: schemas.ProfessorCreate, db: Session=Depends(get_db)): # Criar professor
    db_professor = models.Professor( # Criando uma instancia
        nome = professor.nome,
        email = professor.email
    )
    db.add(db_professor) # Adicinando ao banco de dados
    db.commit() # Confirmando
    db.refresh(db_professor) # Atulizando objeto
    return db_professor

# Rota GET para listar todos os professores
@app.get('/professores', response_model=List[schemas.Professor])
def listar_professores(db: Session=Depends(get_db)): # Lista professores
    professores = db.query(models.Professor).all() # Busca todos os professores na tabela
    if not professores:
        raise HTTPException(status_code=404, detail='Nenhum professor encontrado') # Lança exceção
    return professores

# Rota GET para buscar um professor
@app.get('/professores/', response_model=schemas.Professor)
def consultar_professor(nome_professor: str, db: Session=Depends(get_db)):
    professor = db.query(models.Professor).filter(models.Professor.nome == nome_professor).first() # Busca o professor com nome solicitado
    if not professor:
        raise HTTPException(status_code=404, detail=f'Nenhum {nome_professor} encontrado') # Lança excceção se não econtrado
    return professor

# Rota DELETE para demitir professor
@app.delete('/professores/', response_model=schemas.Professor)
def demitir_professor(id: int, db: Session=Depends(get_db)): # Demiti um professor
    professor = db.query(models.Professor).filter(models.Professor.id == id).first() # Busca pelo ID
    if not professor:
        raise HTTPException(status_code=404, detail='Nenhum professor com esse ID encontrado') # Lança exceção se não encontrado
    db.delete(professor) # Deleta
    db.commit() # Confirma
    return professor # Retorna professor  demitido

# Rota POST para criar disciplina
@app.post('/disciplinas', response_model=schemas.Disciplina)
def criar_disciplina(disciplina: schemas.DisciplinaCreate, db: Session=Depends(get_db)):
    db_disciplina = models.Disciplina(
        nome_disciplina = disciplina.nome_disciplina,
        professor_id = disciplina.professor_id
    )
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina

# Rota GET para listar as disciplinas
@app.get('/disciplinas', response_model=List[schemas.Disciplina])
def listar_disciplinas(db: Session=Depends(get_db)):
    disciplinas = db.query(models.Disciplina).all()
    if not disciplinas:
        raise HTTPException(status_code=404, detail='Nenhuma disciplina cadastrada')
    return disciplinas

# Rota GET para buscar uma disciplina
@app.get('/disciplinas/', response_model=schemas.Disciplina)
def consultar_disciplina(nome_disciplina: str, db: Session=Depends(get_db)):
    disciplina = db.query(models.Disciplina).filter(models.Disciplina.nome_disciplina == nome_disciplina).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail=f'Disciplina {nome_disciplina} não encontrada')
    return disciplina

# Rota DELETE para excluir disciplina
@app.delete('/disciplinas/', response_model=schemas.Disciplina)
def ecluir_disciplina(id: int, db: Session=Depends(get_db)):
    disciplina = db.query(models.Disciplina).filter(models.Disciplina.id == id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail=f'Disciplina não encontrada')
    db.delete(disciplina)
    db.commit()
    return disciplina