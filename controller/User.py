from model.User import User

class UserController():
  def __init__(self):
    self.user_model = User()

  def login(self, email, password):


    # 1. Get the email and save in the user model attribute
    self.user_model.email = email

    # 2. Check if the user exists
    result = self.user_model.get_user_by_email()

    # 3. Check if the password provided matches the password in the database
    if result is not None:
      res = self.user_model.verify_password(password, result.password)

      if res:
        return result
      else:
        return {}
    
    return{}
  
  def recovery(email):
    # It will be created later
    return ''