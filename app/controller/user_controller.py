from flask import Blueprint
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.dto.user import UserDTO
from app.infra.session_manager import SessionLocal

user_bp = Blueprint('users', __file__, url_prefix='/users')


def get_user_service():
    return UserService(UserRepository(SessionLocal()))


@user_bp.route('/', methods=['GET'])
def get_users() -> list[UserDTO]:
    user_service = get_user_service()
    return user_service.list()