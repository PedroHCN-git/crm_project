from fastapi import APIRouter, Response, Form, Depends
from app.services.user_service import UserService, UserServiceInterface
from app.repositories.user_repository import UserRepository, UserRepositoryInterface
from app.dto.user import UserCreateDTO, UserResponseDTO, UserDataActualizeDTO
from app.infra.session_manager import SessionLocal
from app.mappers.user_mapper import UserMapperProtocol, UserMapper

import logging
from sqlalchemy.orm import Session
from typing import Optional

logging.basicConfig(filename='app.log', level=logging.INFO)
logger = logging.getLogger(__name__)

user_router = APIRouter(prefix='/users')


def start_session():
    s = SessionLocal()
    try:
        yield s
    finally:
        s.close()


def get_user_mapper():
    return UserMapper


def get_user_repository(session: Session = Depends(start_session)):
    return UserRepository(session)


def get_user_service(
    repository: UserRepositoryInterface = Depends(get_user_repository),
    mapper: UserMapperProtocol = Depends(get_user_mapper)
):
    return UserService(repository, mapper)


@user_router.get(
    '/',
    response_model=list[UserResponseDTO]
)
async def get_users(
    user_service: UserService = Depends(get_user_service)
) -> list[UserResponseDTO]:
    return user_service.list()


@user_router.get(
    '/{user_id}',
    response_model=Optional[UserResponseDTO]
)
async def get_user(
    user_id: str,
    user_service: UserServiceInterface = Depends(get_user_service)
) -> Optional[UserResponseDTO]:
    try:
        return user_service.get_by_id(user_id)
    except ValueError:
        return Response('User id must be an integer number', status=400)
        


@user_router.post('/')
async def create_user(
    user_data: UserCreateDTO = Form(),
    user_service: UserServiceInterface = Depends(get_user_service)
):
    user_dto = UserCreateDTO(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password
    )

    try:
        user_service.save(user_dto)
        return Response('User created', status_code=201)
    except Exception:
        return Response('User save failed', status_code=400)


@user_router.patch('/{user_id}')
async def actualize_user_data(
    user_id: str,
    user_data: UserDataActualizeDTO = Form(),
    user_service: UserServiceInterface = Depends(get_user_service)
):
    try:
        user_service.actualize_data(user_id, user_data)
        return Response('Data actualized', status_code=200)
    except Exception:
        return Response('Actualize failed', status_code=400)
