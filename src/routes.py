from flask import Blueprint
from src.controller.authentication_controller import login_user,register_user

unprotected_routes = Blueprint('unprotected_routes', __name__)

unprotected_routes.route('/login', methods=['POST'])(login_user)
unprotected_routes.route('/register', methods=['POST'])(register_user)
