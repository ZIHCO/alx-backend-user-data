#!/usr/bin/env python3
"""basic authorization"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """implement basicauth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """implement base64 encoding"""
        if not authorization_header:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[0:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """implement base64 decoding"""

        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_obj = base64.b64decode(base64_authorization_header)
            return decoded_obj.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decode_base64_authorization_header: str
                                 ) -> (str, str):
        """extract users credential"""

        if not decode_base64_authorization_header:
            return (None, None)
        if type(decode_base64_authorization_header) is not str:
            return (None, None)
        if ":" not in decode_base64_authorization_header:
            return (None, None)
        list_credentials = decode_base64_authorization_header.split(":")
        if len(list_credentials) > 2:
            passwd = ""
            for i in range(1, len(list_credentials)):
                passwd += list_credentials[i]
                if i != len(list_credentials) + 1:
                    passwd += ":"
            return (list_credentials[0], passwd)
        return (list_credentials[0], list_credentials[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str,
                                     ) -> TypeVar('User'):
        """build user obj from users credentials"""

        if not user_email or type(user_email) is not str:
            return None
        if not user_pwd or type(user_pwd) is not str:
            return None
        try:
            student = User.search({'email': user_email})
            if student[0].is_valid_password(user_pwd):
                return student[0]
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves User instance"""
        _header = self.authorization_header(request)
        b64_head = self.extract_base64_authorization_header(_header)
        str_decode = self.decode_base64_authorization_header(b64_head)
        tuple_credentials = self.extract_user_credentials(str_decode)
        email, passwd = tuple_credentials
        return self.user_object_from_credentials(email, passwd)
