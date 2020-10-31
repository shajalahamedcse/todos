from flask import Blueprint
from src.utils import ResponseGenerator

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route("/api/v1/register")
def register():
    return ResponseGenerator.generate_response("Hell0", 200)

@user_blueprint.route("/api/v1/login")
def login():
    return ResponseGenerator.generate_response("Hell0", 200)