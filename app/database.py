"""
Configuração da conexão com o banco de dados via SQLAlchemy.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# URL do banco (padrão: SQLite local)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# Para SQLite precisamos do connect_args, para outros bancos não
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Dependency para obter sessão do banco nas rotas."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
