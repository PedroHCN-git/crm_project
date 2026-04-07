from flask import Blueprint, request, Response, jsonify
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.dto.user import UserCreateDTO, UserResponseDTO
from app.infra.session_manager import SessionLocal
import logging
from typing import Optional

logging.basicConfig(filename='app.log', level=logging.INFO)
logger = logging.getLogger(__name__)

user_bp = Blueprint('users', __file__, url_prefix='/users')


def start_session():
    return SessionLocal()


def get_user_service():
    return UserService(
        UserRepository(
            start_session()
        )
    )


user_service = get_user_service()


@user_bp.route('/', methods=['GET'])
def get_users() -> list[UserResponseDTO]:
    return user_service.list()


@user_bp.route('/<user_id>')
def get_user(user_id: str) -> Optional[UserResponseDTO]:
    try:
        return user_service.get_by_id(user_id).model_dump_json()
    except ValueError:
        return Response('User id must be an integer number', status=400)
        


@user_bp.route('/', methods=['POST'])
def create_user():
    user_dto = UserCreateDTO(
        name=request.form.get('name'),
        email=request.form.get('email'),
        password=request.form.get('password')
    )

    try:
        user_service.save(user_dto)
    except Exception:
        return Response('User save failed', status=400)