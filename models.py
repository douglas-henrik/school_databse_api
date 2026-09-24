from sqlalchemy import Column, Integer, String, ForeignKey # Importando os tipos de atributos
from sqlalchemy.orm import relationship # Importando relação entre tabelas
from database import Base # Importando a Base do DataBase

class Estudante(Base): # Criando classe estudante, referencia-se a tabela estudantes
    __tablename__ = 'estudantes' # Defino nome da tabela
    id = Column( # Coluna ID
        Integer, # Tipo int
        primary_key=True, # Primary Key
        index=True # Auto-preenche
    )
    nome = Column( # Coluna nome
        String(50), # Tipo str
        nullable=False # Não pode ficar vazio
    )
    email = Column( # Coluna email
        String(100), 
        nullable=False
    )
    perfil = relationship( # Atributo de relação
        "Perfil", # Relação com a Class Perfill
        back_populates='estudante', # Atributo dessa classe
        uselist=False, # 1:1, Estudante so pode ter 1 perfil
        cascade='all, delete-orphan' # Se esse estudante for removido, apaga tudo que tem relação com ele
    )

class Perfil(Base): # Criando classe Perfil
    __tablename__ = 'perfis' # Nome da tabela
    id = Column( # Coluna ID
        Integer,
        primary_key=True,
        index=True
    )
    idade = Column( # Coluna Idade
        Integer,
        nullable=False
    )
    endereco = Column( # Coluan Endereço
        String(100),
        nullable=False
    )
    estudante_id = Column( # Coluna de Estudante
        Integer,
        ForeignKey('estudantes.id'), # Refere-se ao estudante cujo id seja igual a esse
        unique=True # So pode ter um estudante, outro perfil nao pode ter mesmo estudante
    )
    estudante = relationship( # Atributo de relação
        'Estudante', # Relação com a classe Estudante
        back_populates='perfil' # Atributo dessa classe
    )
