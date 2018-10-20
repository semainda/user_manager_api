"""Module that runs the flask app"""
# system imports
import os

# local imports
from app import UserManager

ENV_CONFIG = os.getenv("ENV_CONFIG")  # load env config

APP = UserManager(ENV_CONFIG)

APP = APP.create_app()

if __name__ == "__main__":
    APP.run()

