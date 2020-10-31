from flask import Blueprint
from src.utils import ResponseGenerator
from src.core.database import app


home_blueprint = Blueprint('index', __name__)

@home_blueprint.route("/")
def home():
    return ResponseGenerator.generate_response("Hell0", 200)