from app.model import User

class UserController:
    def __init__(self):
        self.user_model = User()


    def login(self, email, password):
        self.user_model.email = email
        result = self.user_model.get_user_by_email(email)

        if result is not None:
            if self.user_model.verify_password(password):
                return result
            else:
                return {}
        else:
            return {}

    
    def recovery_password(self, email):
        pass