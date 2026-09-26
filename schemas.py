from typing import List, Optional # Importando Lista e Optional
from pydantic import BaseModel # Importando BaseModel

class Perfil(BaseModel): # Validação do perfil
    id: int # tem que ser int
    idade: int # tem que ser int
    endereco: str # tem que ser str

    class Config:
        from_attributes = True

class PerfilCreate(BaseModel): # Validando a criação de perfil
    idade: int # Precisa da idade
    endereco: str # Precisa do endereço

class Estudante(BaseModel): # Validação do estudante
    id: int # Id tem que ser Interio
    nome: str # Nome tem que ser String
    email: str # Email tem que ser String
    perfil: Perfil # Peril é do estudante

    class Config: # Traz as informações dos estudantes
        from_attributes = True

class EstudanteCreate(BaseModel): # Validando a crianção de estudantes
    nome: str # Precisa do nome
    email:str # Precisa do email
    perfil: PerfilCreate # Cria um perfil

class Professor(BaseModel): # Validando professores
    id: int # Tem que ser int
    nome: str # Tem que ser str
    email: str # Tem que ser str

    class Config: # Traz as informações dos estudantes
        from_attributes = True

class ProfessorCreate(BaseModel): # Validando criação de professores
    nome: str # Precisa do nome
    email: str # Precisa do email

class Disciplina(BaseModel): # Validando disciplinas
    id: int # Tem que ser int
    nome_disciplina: str # Tem que ser str
    professor_id: Optional[int] = None # Opicinal

    class Config: # Traz as informações dos estudantes
        from_attributes = True

class DisciplinaCreate(BaseModel): # Validando a criação de disciplinas
    nome_disciplina: str # Tem que ser str
    professor_id: Optional[int] = None # Opcional

class Matricula(BaseModel): # Validando Matricula
    id: int # Tem que ser int
    estudante_id: int # Tem que ser int
    disciplina_id: int # Tem que ser int

class MatriculaCreate(BaseModel): # Validando criação de matriculas
    estudante_id: int # Tem que ser int
    disciplina_id: int # Tem que ser int