from fastapi import HTTPException
from starlette import status
from starlette.requests import Request

from services.users.src.infrastructure.security import TokenService, TokenServiceImpl


def get_token_service() -> TokenService:
    return TokenServiceImpl()


def get_token_from_header(request: Request) -> str:
    auth = request.headers.get("Authorization")

    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header",
        )

    return auth.split(" ", 1)[1]
