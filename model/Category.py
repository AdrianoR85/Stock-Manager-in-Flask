from extensions import db

from flask_sqlalchemy import SQLAlchemy
from model.User import User

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  description = db.Column(db.Text(), nullable=True)

  def __repr__(self):
    return self.name