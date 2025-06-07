from extensions import db
from .Role import Role
from passlib.hash import  pbkdf2_sha256


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(40), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
  last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=True)
  recovery_code = db.Column(db.String(200), nullable=True)
  status = db.Column(db.Integer, default=1, nullable=True)

  role = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)

  def get_user_by_email(self):
    ...
  
  def get_user_by_id(self):
    ...
  
  def get_update(self, obj):
    ...
  
  def hash_password(self, password):
    try:
      return pbkdf2_sha256.hash(password)
    except Exception as e:
      print(f"Error encrypting password {e}")

  def set_password(self, password):
    self.password = pbkdf2_sha256.hash(password)
  
  def verify_password(self, password_no_hash, password_database):
    try:
      return pbkdf2_sha256.verify(password_no_hash, password_database)
    except ValueError:
      return False