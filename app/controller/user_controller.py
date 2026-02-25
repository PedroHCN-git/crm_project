from flask import Blueprint
from app.services.user_service import UserService

def create_bp(user_service: UserService):
    bp = Blueprint(__file__, 'User', url_prefix='/user')

    @bp.route('/', methods=['GET'])
    def get_users():
        pass