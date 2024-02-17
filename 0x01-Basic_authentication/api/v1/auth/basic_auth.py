#!/usr/bin/env python3
"""basic authorization"""
from api.v1.auth.auth import Auth


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
        """implement base64 encoding"""
        import base64

        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_obj = base64.b64decode(base64_authorization_header)
            return decoded_obj.decode('utf-8')
        except Exception:
            return None
