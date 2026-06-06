<div align="center">

# 🚀 FastAPI REST Boilerplate

**Template profissional de API REST com JWT, CRUD completo e Swagger**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-orange)](https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github)](https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate)

</div>

---

## 📌 Sobre o projeto

Template profissional de API REST em FastAPI, pronto para uso em produção. Inclui **autenticação JWT**, operações CRUD completas, banco de dados com SQLAlchemy, validação com Pydantic e documentação automática via Swagger — tudo estruturado de forma modular e escalável.

### Funcionalidades

- ✅ **Autenticação JWT** — registro, login e proteção de rotas
- ✅ **CRUD completo** de usuários e itens
- ✅ **SQLAlchemy ORM** com SQLite (trocável para PostgreSQL/MySQL)
- ✅ **Validação automática** com Pydantic v2
- ✅ **Hash seguro de senhas** com bcrypt
- ✅ **Swagger UI** automático em `/docs`
- ✅ **Estrutura modular** e escalável com routers
- ✅ **CORS configurado** para integração com frontend

---

## 🛠️ Tecnologias

- **FastAPI** — Framework web moderno e performático
- **SQLAlchemy** — ORM para banco de dados
- **Pydantic** — Validação e serialização de dados
- **python-jose** — Geração e validação de tokens JWT
- **passlib + bcrypt** — Hash seguro de senhas
- **Uvicorn** — Servidor ASGI

---

## 📁 Estrutura

```
fastapi-rest-boilerplate/
├── app/
│   ├── main.py              # Ponto de entrada
│   ├── database.py          # Configuração do banco
│   ├── models.py            # Modelos SQLAlchemy
│   ├── schemas.py           # Schemas Pydantic
│   ├── auth.py              # Lógica JWT
│   └── routers/
│       ├── users.py         # Endpoints de usuários
│       └── items.py         # Endpoints de itens (CRUD)
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📦 Instalação

```bash
git clone https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate.git
cd fastapi-rest-boilerplate

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt

cp .env.example .env
# Edite .env e configure SECRET_KEY

uvicorn app.main:app --reload
```

Acesse **http://localhost:8000/docs** para a documentação interativa.

---

## 📡 Endpoints

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/auth/register` | Registrar novo usuário |
| `POST` | `/auth/login` | Login — retorna token JWT |

### Usuários *(autenticado)*
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/users/me` | Dados do usuário autenticado |

### Itens *(autenticado)*
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/items/` | Listar todos os itens |
| `POST` | `/items/` | Criar novo item |
| `GET` | `/items/{id}` | Obter item por ID |
| `PUT` | `/items/{id}` | Atualizar item |
| `DELETE` | `/items/{id}` | Deletar item |

---

## ⚡ Exemplo de uso via cURL

```bash
# Registrar
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

Pronto para deploy em:
- **Railway**, **Render**, **Fly.io** — gratuitos
- **AWS**, **Google Cloud**, **Azure**
- **Docker** — adicionar Dockerfile conforme necessidade

---

## ✅ Requisitos

- Python **3.11** ou superior

---

## 👤 Autor

<div align="center">

**Wagner Lacerda** — Python Backend Developer | APIs REST • Automação • Data Engineering

[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github&logoColor=white)](https://github.com/LacerdaTraderCode)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner%20Lacerda-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/wagner-lacerda-da-silva-958b9481)
[![YouTube](https://img.shields.io/badge/YouTube-LacerdaTraderCode-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@LacerdaTraderCode)
[![Telegram](https://img.shields.io/badge/Telegram-LacerdaTraderCode-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode)
[![Telegram Bots](https://img.shields.io/badge/Telegram-Bots-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode_bots)

📍 Rio Grande do Sul, Brasil

</div>

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
