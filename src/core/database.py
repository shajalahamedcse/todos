from flask import Flask
from flask_cors import CORS
from src.core.config import Configuration

app = Flask(__name__)
CORS(app)
app.config.from_object(Configuration)