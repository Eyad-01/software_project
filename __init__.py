from flask import Flask
from src.routes import unprotected_routes
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

app.register_blueprint(unprotected_routes)
