<div align="center">

# 🚀 FastAPI REST Boilerplate

**A professional REST API template with JWT, full CRUD, and Swagger**

[![CI](https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-orange)](https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github)](https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate)

</div>

---

## 📌 About the Project

A professional, production-ready REST API template built with FastAPI. Includes **JWT authentication**, full CRUD operations, a SQLAlchemy-backed database, Pydantic validation, and automatic Swagger documentation — all structured in a modular, scalable way.

### Features

- ✅ **JWT authentication** — registration, login, and route protection
- ✅ **Full CRUD** for users and items
- ✅ **SQLAlchemy ORM** with SQLite (swappable for PostgreSQL/MySQL)
- ✅ **Automatic validation** with Pydantic v2
- ✅ **Secure password hashing** with bcrypt
- ✅ **Automatic Swagger UI** at `/docs`
- ✅ **Modular, scalable structure** with routers
- ✅ **CORS configured** for frontend integration

---

## 🛠️ Technologies

- **FastAPI** — Modern, high-performance web framework
- **SQLAlchemy** — Database ORM
- **Pydantic** — Data validation and serialization
- **python-jose** — JWT token generation and validation
- **passlib + bcrypt** — Secure password hashing
- **Uvicorn** — ASGI server

---

## 📁 Structure

```
fastapi-rest-boilerplate/
├── app/
│   ├── main.py              # Entry point
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── auth.py              # JWT logic
│   └── routers/
│       ├── users.py         # User endpoints
│       └── items.py         # Item endpoints (CRUD)
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/LacerdaTraderCode/fastapi-rest-boilerplate.git
cd fastapi-rest-boilerplate

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt

cp .env.example .env
# Edit .env and set SECRET_KEY

uvicorn app.main:app --reload
```

Visit **http://localhost:8000/docs** for the interactive documentation.

---

## 📡 Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-----------|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Login — returns a JWT token |

### Users *(authenticated)*
| Method | Endpoint | Description |
|--------|----------|-----------|
| `GET` | `/users/me` | Authenticated user's data |

### Items *(authenticated)*
| Method | Endpoint | Description |
|--------|----------|-----------|
| `GET` | `/items/` | List all items |
| `POST` | `/items/` | Create a new item |
| `GET` | `/items/{id}` | Get item by ID |
| `PUT` | `/items/{id}` | Update item |
| `DELETE` | `/items/{id}` | Delete item |

---

## ⚡ Usage Example via cURL

```bash
# Register
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=password123"

# Use token
curl -X GET "http://localhost:8000/items/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

---

## 🚀 Deploy

Ready for deployment on:
- **Railway**, **Render**, **Fly.io** — free tiers
- **AWS**, **Google Cloud**, **Azure**
- **Docker** — add a Dockerfile as needed

---

## ✅ Requirements

- Python **3.11** or higher

---

## 👤 Author

<div align="center">

**Wagner Lacerda** — Senior Software Engineer | Python, Backend, AI Apps, Automation & Systems

[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github&logoColor=white)](https://github.com/LacerdaTraderCode)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner%20Lacerda-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/wagner-lacerda-da-silva-958b9481)
[![YouTube](https://img.shields.io/badge/YouTube-LacerdaTraderCode-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@LacerdaTraderCode)
[![Telegram](https://img.shields.io/badge/Telegram-LacerdaTraderCode-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode)
[![Telegram Bots](https://img.shields.io/badge/Telegram-Bots-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode_bots)

📍 Rio Grande do Sul, Brazil

</div>

---

## 📄 License

Distributed under the MIT license. See [LICENSE](LICENSE) for more details.
