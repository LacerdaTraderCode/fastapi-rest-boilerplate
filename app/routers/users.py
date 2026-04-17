"""
Router de usuários - endpoints relacionados ao usuário autenticado.
"""
from fastapi import APIRouter, Depends

from app.models import User
from app.schemas import UserResponse
from app.auth import get_current_user

router = APIRouter()


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    """Retorna dados do usuário autenticado."""
    return current_user
