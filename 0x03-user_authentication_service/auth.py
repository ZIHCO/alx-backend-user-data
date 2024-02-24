#!/usr/bin/env python3
"""authentication implimented"""
import bcrypt
import base64

def _hash_password(password: str) -> bytes:
    """hash password"""
    if password:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)
