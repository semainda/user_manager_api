"""Module that defines users views"""
from flask_restful import Resource, reqparse

from app.api.v1.models.users.users import UserModel

PARSER = reqparse.RequestParser()
      
PARSER.add_argument(
    "first_name", required=True, type=str, help="Key first_name not found")
PARSER.add_argument(
    "last_name", required=True, type=str, help="Key last_name not found")
PARSER.add_argument(
    "email", required=True, type=str, help="Key email not found")
PARSER.add_argument(
    "password", required=True, type=str, help="Key password not found")


class Users(Resource):
    """Class that defines users endpoints"""
    def __init__(self):
        self.user = UserModel()
    
    def post(self):
        """Method that creates users"""
        data_parsed = PARSER.parse_args()
        user = self.user.create_user(
            data_parsed["first_name"],
            data_parsed["last_name"],
            data_parsed["email"],
            data_parsed["password"]
        )
        return {"User": "{} created successful".format(user)}, 200
