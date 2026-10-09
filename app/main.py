from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import auth, items, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI REST Boilerplate",
    description="REST API template with JWT authentication and CRUD",
    version="1.0.0",
    contact={
        "name": "Wagner Lacerda",
        "url": "https://github.com/LacerdaTraderCode",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])


@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "FastAPI REST Boilerplate is running",
        "docs": "/docs",
        "version": "1.0.0",
    }


@app.get("/health", tags=["Root"])
def health_check():
    return {"status": "healthy"}
