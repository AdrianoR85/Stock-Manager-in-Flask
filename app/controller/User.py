from unittest import result
from app.model import User
from app.extensions import logger

import jwt
from datetime import datetime, timedelta
from config import Config


class UserController:
    @staticmethod
    def login(email, password):
        user = User.get_by_email(email)

        if user is not None:
            if user.verify_password(password):
                return user
        
        return {}
    
    @staticmethod
    def total_users():
        result = {}
        try:
            result['data'] = User.count_users()
            result['status'] = 200
        except Exception as e:
            logger.exception("Error fetching total users")
            result['status'] = 500
            result['message'] = str(e)
        return result
    
    @staticmethod
    def verify_auth_token(token):
        try:
            payload = jwt.decode(
                token,
                Config.SECRET_KEY,
                algorithms=["HS256"]
            )

            return {
                "status": 200,
                "message": "Token válido",
                "data": payload
            }

        except jwt.ExpiredSignatureError:
            return {
                "status": 401,
                "message": "Token expirado"
            }

        except jwt.InvalidTokenError:
            return {
                "status": 401,
                "message": "Token inválido"
            }

    @staticmethod
    def generate_auth_token(data, exp=30):
        
        expiration = datetime.now(datetime.timezone.utc) + timedelta(minutes=exp)

        payload = {
            "id": data["id"],
            "username": data["username"],
            "exp": expiration
        }

        return jwt.encode(
            payload,
            Config.SECRET_KEY,
            algorithm="HS256"
        )
