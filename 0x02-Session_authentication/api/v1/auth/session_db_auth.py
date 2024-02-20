#!/usr/bin/env python3
"""session DB Authentication"""
from flask import request
from datetime import datetime
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """DB authentication"""
    def create_session(self, user_id=None):
        """create and stores new instance of UserSession"""
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        kwargs = {
                  "user_id": user_id,
                  "session_id": session_id
                  }
        user_session = UserSession(**kwargs)
        if not user_session:
            return None
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """returns userID from UserSession in DB"""
        if not session_id:
            return None
        try:
            user_session = UserSession.search({"session_id": session_id})[0]
        except Exception:
            return None
        if ((user_session.created_at.second + self.session_duration) <
           datetime.now().second):
            return None
        return user_session.to_json().get("user_id")

    def destory_session(self, request=None):
        """destroys the usersession based on the session_id"""
        if not request:
            return False
        try:
            session_id = self.session_cookie(request)
            if not session_id:
                return False
            user_session = UserSession.search({"session_id": session_id})[0]
        except Exception:
            return False
        if not user_session:
            return False
        del type(self).user_id_by_session-id[user_session]
        return True
