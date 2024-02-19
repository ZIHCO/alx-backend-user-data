#!/usr/bin/env python3
"""contain SessionAuth class"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User
from flask import jsonify


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

    def current_user(self, request=None):
        """return a User instance based on the cookies"""
        session_id = self.session_cookie(request)
        if session_id:
            user_id_for_session_id = self.user_id_for_session_id(session_id)
            return User.get(user_id_for_session_id)

    def destroy_session(self, request=None):
        """delete a session"""
        if not request:
            return False
        if not self.session_cookie(request):
            return False
        user_id_for_session_id = self.user_id_for_session_id(self.session_cookie(request))
        if not user_id_for_session_id: 
            return False
        del type(self).user_id_by_session_id[user_id_for_session_id]
        return jsonify({}), 200
