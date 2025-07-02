from abc import ABC

from services.news.src.domain.models import Post
from services.shared.interface.repositories import AbstractRepository


class PostRepository(AbstractRepository[Post], ABC):
    pass

