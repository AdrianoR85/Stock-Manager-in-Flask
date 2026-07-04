from flask_admin import Admin
from app.extensions import ModelView
from flask_admin.theme import Bootstrap4Theme

from app.model import Role, User, Category, Product
from app.admin.Views import UserView

all_themes = [
  "default", "cerulean", "cosmo", "cyborg",  "darkly",
  "flatly", "journal", "litera", "lumen", "lux", "materia",
  "minty", "pulse", "sandstone", "simplex", "sketchy", "slate",
  "solar", "spacelab",  "superhero", "united", "yeti"
]

def start_views(app, db):
    admin = Admin(app, name="Meu Estoque", theme=Bootstrap4Theme(swatch="lux"))

    admin.add_view(ModelView(Role, db.session, "Funções", category="Usuários"))
    admin.add_view(UserView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(ModelView(Category, db.session, "Categorias", category="Produtos"))
    admin.add_view(ModelView(Product, db.session, "Produtos", category="Produtos"))