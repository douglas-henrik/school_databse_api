# 🎓 Escola API

API REST desenvolvida em **Python** utilizando **FastAPI**, **SQLAlchemy** e **PostgreSQL** para gerenciamento de estudantes e seus perfis.

O projeto foi desenvolvido com foco em aprendizado e prática de desenvolvimento de APIs, integração com banco de dados relacional, ORM, validação de dados e criação de rotas HTTP.

## 🚀 Tecnologias utilizadas

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **PostgreSQL**
* **Uvicorn**

## 📚 Funcionalidades

Atualmente, a API permite:

* Criar estudantes e seus respectivos perfis;
* Listar todos os estudantes;
* Buscar um estudante pelo nome;
* Deletar um estudante pelo ID;
* Relacionar um estudante a um perfil;
* Validar os dados recebidos através do Pydantic;
* Persistir os dados em um banco PostgreSQL.

## 🗂️ Estrutura do projeto

```text
escola-api/
│
├── database.py
├── models.py
├── schemas.py
├── main.py
├── requirements.txt
└── README.md
```

### `database.py`

Responsável pela configuração da conexão com o PostgreSQL e pela criação da sessão utilizada pela aplicação.

Principais elementos:

* `engine`
* `Base`
* `SessionLocal`

### `models.py`

Define as entidades do banco de dados utilizando SQLAlchemy.

Atualmente existem duas entidades:

* `Estudante`
* `Perfil`

Existe um relacionamento **1:1** entre estudante e perfil.

### `schemas.py`

Define os schemas utilizados para validação dos dados da API através do Pydantic.

Existem schemas específicos para:

* Criação de estudantes;
* Criação de perfis;
* Resposta de estudantes;
* Resposta de perfis.

### `main.py`

Contém a aplicação FastAPI e as rotas da API.

Também é responsável por:

* Criar as tabelas do banco;
* Gerenciar as sessões do banco;
* Processar as requisições;
* Criar, consultar e excluir estudantes.

## 🔗 Endpoints

### Criar estudante

```http
POST /estudantes
```

Exemplo de requisição:

```json
{
    "nome": "João",
    "email": "joao@email.com",
    "perfil": {
        "idade": 20,
        "endereco": "João Pessoa - PB"
    }
}
```

### Listar estudantes

```http
GET /estudantes
```

Retorna uma lista com os estudantes cadastrados.

### Buscar estudante

```http
GET /estudantes/?nome_estudante=João
```

Busca um estudante pelo nome.

### Deletar estudante

```http
DELETE /estudantes/?id_estudante=1
```

Remove um estudante pelo seu ID.

## 🗄️ Banco de dados

O projeto utiliza **PostgreSQL**.

A aplicação utiliza o SQLAlchemy para realizar a comunicação entre o Python e o banco de dados.

As tabelas são criadas através de:

```python
models.Base.metadata.create_all(bind=engine)
```

### Relacionamento

A estrutura possui um relacionamento de **um para um (1:1)**:

```text
Estudante
    │
    └── Perfil
```

Um estudante possui um perfil, e cada perfil pertence a um único estudante.

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd escola-api
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

Crie um banco PostgreSQL e configure a URL de conexão no arquivo `database.py`.

Exemplo:

```python
DATABASE_URL = "postgresql://usuario:senha@localhost:5432/db_escola"
```

### 5. Executar a API

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

## 📖 Documentação da API

O FastAPI disponibiliza automaticamente uma interface interativa para testar os endpoints.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como parte dos estudos de desenvolvimento backend com Python.

O principal objetivo é praticar conceitos como:

* Desenvolvimento de APIs REST;
* FastAPI;
* ORM com SQLAlchemy;
* PostgreSQL;
* Relacionamentos entre tabelas;
* Pydantic e validação de dados;
* Operações CRUD;
* Injeção de dependências com `Depends`;
* Organização de um projeto backend.

## 🔄 Próximos passos

Algumas melhorias que podem ser implementadas futuramente:

* [ ] Implementar tratamento de estudante não encontrado;
* [ ] Completar as operações CRUD;
* [ ] Melhorar as validações dos dados;
* [ ] Utilizar variáveis de ambiente para as credenciais do banco;
* [ ] Adicionar mais endpoints;
* [ ] Implementar atualização de estudantes;
* [ ] Adicionar testes automatizados;
* [ ] Melhorar o tratamento de erros;
* [ ] Organizar o projeto em uma estrutura maior conforme a API evoluir.

---

**Projeto desenvolvido para fins de estudo e prática de desenvolvimento Backend com Python.**
