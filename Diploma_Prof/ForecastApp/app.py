from app_logger import logger_output
from config import DEBUG
from views import views_handler
from views.index import index_handler
from flask import Flask


def create_app():
    try:
        app = Flask(__name__)
        app.config.from_pyfile('config.py')
        app.register_blueprint(index_handler)
        app.register_blueprint(views_handler)
        return app
    except Exception as err:
        logger_output(str(err), DEBUG, 'error')

