# 🚀 FastAPI REST Boilerplate

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

Template profissional de API REST em FastAPI, pronto para uso em produção. Inclui autenticação JWT, operações CRUD completas, banco de dados com SQLAlchemy, validação com Pydantic e documentação automática via Swagger.

---

## 📋 Funcionalidades

- ✅ **Autenticação JWT** com endpoints de registro e login
- ✅ **CRUD completo** de usuários e itens
- ✅ **SQLAlchemy ORM** com SQLite (facilmente trocável para PostgreSQL/MySQL)
- ✅ **Validação automática** com Pydantic
- ✅ **Hash seguro de senhas** com bcrypt
- ✅ **Documentação Swagger** automática em `/docs`
- ✅ **Estrutura modular** e escalável
- ✅ **CORS configurado** para integração com frontend

---

## 🛠️ Tecnologias

- **FastAPI** — Framework web moderno e performático
- **SQLAlchemy** — ORM para banco de dados
- **Pydantic** — Validação de dados
- **python-jose** — Geração e validação de tokens JWT
- **passlib + bcrypt** — Hash de senhas
- **Uvicorn** — Servidor ASGI

---

## 📁 Estrutura do Projeto

```
fastapi-rest-boilerplate/
├── app/
│   ├── __init__.py
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── database.py          # Configuração do banco de dados
│   ├── models.py            # Modelos SQLAlchemy
│   ├── schemas.py           # Schemas Pydantic
│   ├── auth.py              # Lógica de autenticação JWT
│   └── routers/
│       ├── __init__.py
│       ├── users.py         # Endpoints de usuários
│       └── items.py         # Endpoints de itens (CRUD exemplo)
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Instalação

### Pré-requisitos

- Python 3.11 ou superior

### Passos

```bash
# Clonar repositório
git clone https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate.git
cd fastapi-rest-boilerplate

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite .env e configure SECRET_KEY

# Rodar aplicação
uvicorn app.main:app --reload
```

Acesse: **http://localhost:8000/docs** para a documentação interativa.

---

## 📡 Endpoints Principais

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/auth/register` | Registrar novo usuário |
| POST | `/auth/login` | Login e obtenção de token JWT |

### Usuários (autenticado)
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/users/me` | Obter dados do usuário atual |

### Itens (autenticado)
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/items/` | Listar todos os itens |
| POST | `/items/` | Criar novo item |
| GET | `/items/{id}` | Obter item por ID |
| PUT | `/items/{id}` | Atualizar item |
| DELETE | `/items/{id}` | Deletar item |

---

## 🔒 Exemplo de Uso

```bash
# Registrar usuário
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "senha123"}'

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=senha123"

# Usar token
curl -X GET "http://localhost:8000/items/" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

---

## 🚀 Deploy

Este template está pronto para deploy em:
- **Railway**, **Render**, **Fly.io** (gratuitos)
- **AWS**, **Google Cloud**, **Azure**
- **Docker** (adicionar Dockerfile conforme necessidade)

---

## 👨‍💻 Autor

**Wagner Lacerda**  
🔗 [LinkedIn](https://www.linkedin.com/in/wagner-lacerda-da-silva-958b9481)  
🐙 [GitHub](https://github.com/LacerdaTraderCode)  

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
