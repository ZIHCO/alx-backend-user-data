#!/usr/bin/env python3
"""contain SessionExpAuth"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """manage session expiration"""
    def __init__(self):
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """create session"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dictionary = {
                              "user_id": user_id,
                              "created_at": datetime.now()
                              }
        type(self).user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user ID for session ID"""
        if not session_id:
            return None
        session_dictionary = type(self).user_id_by_session_id.get(session_id)
        if not session_dictionary:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get("user_id")
        created_at = session_dictionary.get("created_at")
        if not created_at:
            return None
        if ((created_at.second + self.session_duration) <
           datetime.now().second):
            return None
        return session_dictionary.get("user_id")
