#!/usr/bin/env python3
"""authentication implimented"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """hash password"""
    if password:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """impliment user registration"""
        if email and password:
            kwargs = {"email": email}
            try:
                user = self._db.find_user_by(**kwargs)
                if user:
                    raise ValueError(f"User {email} already exists")
            except Exception:
                password = _hash_password(password)
                user = self._db.add_user(email, password)
                return user
