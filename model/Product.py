from config import app_active, app_config
from flask_sqlalchemy import SQLAlchemy
from model.Category import Category
from model.User import User

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  description = db.Column(db.Text(), nullable=True)
  qtd= db.Column(db.Integer, nullable=True, default=0)
  image = db.Column(db.Text(), nullable=True)
  price = db.Column(db.Numeric(10,2), nullable=False)
  date_created = db.Column(db.DateTime(6), default=db.func.now(), nullable=False)
  last_update = db.Column(db.DateTime(6), onupdate=db.func.now(), nullable=False)
  status = db.Column(db.Boolean(), default=1, nullable=False)

  user_created = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
  category = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)