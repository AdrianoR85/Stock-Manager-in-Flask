from app.model import User

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
        try:
            return User.count_users()
        except Exception as e:
            print(f"Error occurred while fetching total users: {e}")
            return None