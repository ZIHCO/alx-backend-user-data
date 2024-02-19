#!/usr/bin/env python3
"""contain SessionAuth class"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """Session authentication"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates new session"""
        if not user_id:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid4())
        type(self).user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """return a user ID base on session ID"""
        if not session_id:
            return None
        if type(session_id) is not str:
            return None
        user_id = type(self).user_id_by_session_id.get(session_id)
        return user_id

    def current_user(Self, request=None):
        """return a User instance based on the cookies"""
        session_cookie = self.session_cookie(request)
        if not session_cookie:
            return None
        session_id = session_cookie.get("session_id")
        user_id_for_session_id = self.user_id_for_session_id(session_id)
        if user_id_for_session_id:
            return User.get(user_id=user_id_for_session_id)
