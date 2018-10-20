"""Module that defines flask app"""

# thirdparty imports
from flask import Flask, Blueprint
from flask_restful import Api

# local imports
from instance.config import APP_CONFIG
from .api.v1.views.users.users import Users

API_BLUEPRINT = Blueprint("v1", __name__, url_prefix="/api/v1")
API = Api(API_BLUEPRINT)


class UserManager:
    """Class that creates flask app with specific configs"""
    def __init__(self, config):
        self.app = Flask(__name__, instance_relative_config=True)
        self.app.config.from_object(APP_CONFIG[config])
        # blueprint registration
        self.app.register_blueprint(API_BLUEPRINT)
    
    def create_app(self):
        """Method that return flask instance with given config"""
        return self.app


# endpoints
API.add_resource(Users, "/users")