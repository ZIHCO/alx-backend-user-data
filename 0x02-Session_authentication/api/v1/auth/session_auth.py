#!/usr/bin/env python3
"""contain SessionAuth class"""
from api.v1.auth.auth import Auth
from uuid import uuid4


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