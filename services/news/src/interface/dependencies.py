from fastapi import Depends
from services.news.src.application.usecases.create_post import CreatePostUseCase, CreatePostUseCaseImpl
from services.news.src.application.usecases.delete_post import DeletePostUseCase, DeletePostUseCaseImpl
from services.news.src.application.usecases.find_post import FindPostUseCase, FindPostUseCaseImpl
from services.news.src.application.usecases.find_posts import FindPostsUseCase, FindPostsUseCaseImpl
from services.news.src.application.usecases.update_post import UpdatePostUseCase, UpdatePostUseCaseImpl
from services.news.src.application.validators.create_post import CreatePostValidator
from services.news.src.application.validators.update_post import UpdatePostValidator
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


def get_update_post_use_case(
    uow: PostUnitOfWork = Depends(get_post_unit_of_work),
) -> UpdatePostUseCase:
    return UpdatePostUseCaseImpl(uow)


def get_delete_post_use_case(
    post_repository: PostRepository = Depends(get_post_repository),
) -> DeletePostUseCase:
    return DeletePostUseCaseImpl(post_repository)


def get_find_post_use_case(
    post_repository: PostRepository = Depends(get_post_repository),
) -> FindPostUseCase:
    return FindPostUseCaseImpl(post_repository)


def get_find_posts_use_case(
    post_repository: PostRepository = Depends(get_post_repository),
) -> FindPostsUseCase:
    return FindPostsUseCaseImpl(post_repository)


def get_create_post_validator() -> CreatePostValidator:
    return CreatePostValidator()


def get_update_post_validator() -> UpdatePostValidator:
    return UpdatePostValidator()
