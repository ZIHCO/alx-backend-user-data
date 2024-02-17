#!/usr/bin/env python3
"""basic authorization"""
from api.v1.auth.auth import Auth
import base64


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
        return (list_credentials[0], list_credentials[1])
