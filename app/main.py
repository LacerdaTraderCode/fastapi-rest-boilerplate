"""
FastAPI REST Boilerplate - Ponto de entrada da aplicação.

Este módulo configura a aplicação FastAPI, CORS, e registra as rotas.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.routers import users, items, auth

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializar aplicação
app = FastAPI(
    title="FastAPI REST Boilerplate",
    description="Template profissional de API REST com autenticação JWT",
    version="1.0.0",
    contact={
        "name": "Wagner Lacerda",
        "url": "https://github.com/LacerdaTraderCode",
    },
)

# Configurar CORS (ajuste allow_origins em produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(users.router, prefix="/users", tags=["Usuários"])
app.include_router(items.router, prefix="/items", tags=["Itens"])


@app.get("/", tags=["Root"])
def read_root():
    """Endpoint raiz - health check."""
    return {
        "message": "FastAPI REST Boilerplate está rodando!",
        "docs": "/docs",
        "version": "1.0.0",
    }


@app.get("/health", tags=["Root"])
def health_check():
    """Endpoint de health check para monitoramento."""
    return {"status": "healthy"}
