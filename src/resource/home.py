from flask import Blueprint
from src.utils import ResponseGenerator

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route("/")
def home():
    return ResponseGenerator.generate_response("Hell0", 200)