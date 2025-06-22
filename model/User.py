from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from config import app_active, app_config
from passlib.hash import pbkdf2_sha256
from model.Role import Role

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(40), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  date_created = db.Column(db.DateTime(6), default=db.func.now(), nullable=False)
  last_update = db.Column(db.DateTime(6), onupdate=db.func.now(), nullable= True)
  recovery_code = db.Column(db.String(200), nullable=True)
  active = db.Column(db.Boolean(), default=1, nullable=True)
  
  role = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)

  funcao = relationship(Role)

  def __repr__(self):
    return f"{self.id}-{self.username}"

  def get_user_by_email(self):
    """
    It will be built later 
    """
    return ''
  
  def get_user_by_id(self, id):
    """
    It will be built later 
    """
    return ''

  def update(self, obj):
    """
    It will be built later 
    """
    return ''
  
  def hash_password(self, password):
    try:
      return pbkdf2_sha256.hash(password)
    except Exception as e:
      print(f'Error trying to encrypt the password {password}')
  
  def set_password(self, password):
    self.password = pbkdf2_sha256.hash(password)
  
  def verify_password(self, hash_password, database_password):
    try:
      return pbkdf2_sha256.verify(hash_password, database_password)
    except ValueError:
      return False

  