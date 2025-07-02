from fastapi import Depends

from services.news.src.application.usecases.create_post import CreatePostUseCase, CreatePostUseCaseImpl
from services.news.src.domain.repositories import PostRepository
from services.news.src.domain.uow import PostUnitOfWork
from services.news.src.infrastructure.database import get_session
from services.news.src.infrastructure.repositories import PostRepositoryImpl
from services.news.src.infrastructure.uow import PostUnitOfWorkImpl
from sqlalchemy.orm import Session


def get_post_repository(session: Session = Depends(get_session)) -> PostRepository:
    return PostRepositoryImpl(session)


def get_post_unit_of_work(
    session: Session = Depends(get_session), post_repository: PostRepository = Depends(get_post_repository)
) -> PostUnitOfWork:
    return PostUnitOfWorkImpl(session, post_repository)


def get_create_post_use_case(
    post_repository: PostRepository = Depends(get_post_repository),
) -> CreatePostUseCase:
    return CreatePostUseCaseImpl(post_repository)
