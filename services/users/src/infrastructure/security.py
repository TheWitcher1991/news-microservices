from abc import ABC, abstractmethod


class TokenService(ABC):
    @abstractmethod
    def encode(self, user_id: int) -> str: ...
    @abstractmethod
    def decode(self, token: str) -> int: ...


class TokenServiceImpl(TokenService):
    def encode(self, user_id: int) -> str:
        return str(user_id)

    def decode(self, token: str) -> int:
        return int(token)
