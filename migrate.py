from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_active, app_config
from extensions import db

config = app_config[app_active]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

class Role(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40), unique=True, nullable=True)


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


class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  description = db.Column(db.Text(), nullable=True)


class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  description = db.Column(db.Text(), nullable=True)
  qtd= db.Column(db.Integer, nullable=True, default=0)
  image = db.Column(db.Text(), nullable=True)
  price = db.Column(db.Numeric(10,2), nullable=False)
  date_created = db.Column(db.DateTime(6), default=db.func.now(), nullable=False)
  last_update = db.Column(db.DateTime(6), onupdate=db.func.now())
  status = db.Column(db.Boolean(), default=1, nullable=False)

  user_created = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
  category = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
  app.run()