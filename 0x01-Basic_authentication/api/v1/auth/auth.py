#!/usr/bin/env python3
"""script contains the Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """implements Basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """authentication"""
        if not excluded_paths:
            return True
        if not path:
            return True
        if path not in excluded_paths:
            for item in Excluded_paths:
                if "*" in item:
                    if item[0:-1] in path:
                        break
            else:
                return True
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
