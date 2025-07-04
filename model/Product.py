from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from extensions import db

from model.Category import Category
from model.User import User


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

  usuario = relationship(User)  
  categoria = db.relationship(Category)

  def get_all():
    try:
      res = db.session.query(Product).all()
    except Exception as e:
      res = []
      print(e)
    finally:
      db.session.close()
      return res
  
  def save(self):
    try:
      db.session.add(self)
      db.session.commit()
      return True
    except Exception as e:
      print(e)
      db.session.rollback()
      return False
    
  def update(self, obj):
    try:
      res = db.session.query(Product).filter(Product.id==self.id).update(obj)
      db.session.commit()
      return True
    except Exception as e:
      print(e)
      db.session.rollback()
      return False