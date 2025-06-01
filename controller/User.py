from model.User import User

class UserController():
  def __init__(self):
    self.user_model = User()
  
  def login(self, email, password):
    # get the email data and saves it in the user model attribute 
    self.user_model.email = email

    # Check if the user exists in the database
    result = self.user_model.get_user_by_email()
    # If the user exists the result won't be None
    
    if result is None:
      # Check if the password thar user send to converted to hash is equal to the password from database  
      res = self.user_model.verify_password(password, result.password)

      # if it is equal it returns True
      if res:
        return result
      else:
        return {}
    return {}
  
  def recovery(email):
    """
    Email recovery it will be created in covered 11
    """
