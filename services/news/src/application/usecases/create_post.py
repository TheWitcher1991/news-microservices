from abc import abstractmethod

from services.news.src.domain.models import Post
from services.news.src.domain.repositories import PostRepository
from services.shared.interface.usecases import AbstractUseCase


class CreatePostUseCase(AbstractUseCase):

    @abstractmethod
    def execute(self, title: str, description: str = None) -> Post: ...


class CreatePostUseCaseImpl(CreatePostUseCase):
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, title: str, description: str = None) -> Post:
        post = Post.create(title=title, description=description)
        self.post_repository.create(post)
        return post
