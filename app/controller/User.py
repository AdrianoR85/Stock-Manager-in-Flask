from unittest import result
from app.model import User
from app.extensions import logger

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