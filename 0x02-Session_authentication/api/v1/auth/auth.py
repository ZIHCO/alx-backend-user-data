#!/usr/bin/env python3
"""script contains the Auth class"""
from flask import request, jsonify
from typing import List, TypeVar
from os import getenv


class Auth:
    """implements Basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """authentication"""
        if not excluded_paths:
            return True
        if not path:
            return True
        if path not in excluded_paths:
            if (path + '/') not in excluded_paths:
                return True
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if not request:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None

    def session_cookie(self, request=None):
        """cookie value"""
        if not request:
            return None
        if getenv("SESSION_NAME", "_my_session_id"):
            return request.cookies.get(getenv("SESSION_NAME", "_my_session_id")).to_json()
