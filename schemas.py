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
    perfil: Optional[Perfil] = None # Peril é opcional

    class Config: # Traz as informações dos estudantes
        from_attributes = True

class EstudanteCreate(BaseModel): # Validando a crianção de estudantes
    nome: str # Precisa do nome
    email:str # Precisa do email
    perfil: PerfilCreate # Cria um perfil