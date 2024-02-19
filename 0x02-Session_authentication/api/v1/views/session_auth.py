#!/usr/bin/env python3
"""view that handles session authentication"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login user"""
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "email missing"}), 400
    passwd = request.form.get("password")
    if not passwd:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(passwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].to_json().get("id"))
    output = jsonify(user[0].to_json())
    output.set_cookie(getenv('SESSION_NAME'), session_id)
    return output


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout user"""
    from api.v1.app import auth
    delete_session = auth.destroy_session(request)
    if not delete_session:
        abort(404)
    return delete_session
