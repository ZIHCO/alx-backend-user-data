#!/usr/bin/env python3
"""script contains the Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """implements Basic authentication"""
    def require_auth(self, path: str, excluded_paths: List[str])) -> bool:
        """authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
