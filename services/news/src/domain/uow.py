from abc import ABC

from services.news.src.domain.repositories import PostRepository
from services.shared.interface.uow import AbstractUnitOfWork


class PostUnitOfWork(AbstractUnitOfWork[PostRepository], ABC):
    pass
