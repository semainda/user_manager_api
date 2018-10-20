"""Module that define users model"""
from passlib.hash import pbkdf2_sha256 as hash256
from app.database.db import users

class UserModel:
    """
        Class that represents users table with following
        user_id
        first_name
        last_name
        email
        password
    """
    def __init__(self):
        self.user_id = len(users) + 1

    def create_user(self, first_name, last_name, email, password):
        """Method that creaates a new user"""
        user = dict(
            user_id=self.user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hash256.hash(password)
        )
        users.append(user)
        return users[self.user_id-1]

    def get_users(self):
        """Method that """
        return users
