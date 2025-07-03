from abc import abstractmethod
from typing import List

from services.news.src.domain.models import Post
from services.news.src.domain.repositories import PostRepository
from services.shared.interface.usecases import AbstractUseCase


class FindPostsUseCase(AbstractUseCase):

    @abstractmethod
    def execute(self) -> List[Post]: ...


class FindPostsUseCaseImpl(FindPostsUseCase):
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self) -> List[Post]:
        return self.post_repository.find_all()