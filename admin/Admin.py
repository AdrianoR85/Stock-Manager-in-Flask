from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from model.Role import Role
from model.User import User
from model.Category import Category
from model.Product import Product

def start_views(app, db):
  admin = Admin(app, name="Meu Estoque", template_mode="bootstrap3")

  admin.add_view(ModelView(Role,db.session, name="Funções", category="Usuários"))
  admin.add_view(ModelView(User, db.session, name="Usuários", category="Usuários"))
  admin.add_view(ModelView(Category, db.session, name="Categorias", category="Produtos"))
  admin.add_view(ModelView(Product, db.session, name="Produtos", category="Produtos"))