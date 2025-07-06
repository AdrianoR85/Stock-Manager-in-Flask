from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from config import app_active, app_config
from model.User import User
from model.Category import Category
from model.Product import Product

config = app_config[app_active]

class HomeView(AdminIndexView):
  @expose('/')
  def index(self):
    user_model = User()
    category_model = Category()
    product_model = Product()

    users = user_model.get_total_users()
    categories = category_model.get_total_categories()
    products = product_model.get_total_Products()

    return self.render('home_admin.html', report={
      'users':0 if not users else users[0],
      'categories':0 if not categories else categories[0],
      'products':0 if not products else products[0]
    })

class UserView(ModelView):
  column_exclude_list = ['password', 'recovery_code'] # Remove from visualization
  form_excluded_columns = ['last_update', 'recovery_code']
  form_columns = ['funcao', 'username', 'email', 'password', 'date_created', 'active']

  form_widget_args = {
    'password': {
      'type': 'password'
    }
  }

  column_labels = {
    'funcao': 'Função',
    'username': 'Nome de usuário',
    'email': 'Email',
    'date_created': 'Data de criação',
    'last_update': 'Date de atualização',
    'active': 'Ativo',
    'password': 'Senha'
  }

  column_descriptions = {
    'funcao': 'Função no painel adminstrativo',
    'username': 'Nome de usuário no sistema',
    'email': 'Email do usuário no sistema',
    'date_created': 'Data de criação do usuario no sistema',
    'last_update': 'Última atualização desse usuário no sistema',
    'active': 'Estado ativo ou inativo no sistema',
    'password': 'Senha do usuário no sistema'
  }

  can_set_page_size=True
  can_view_details=True
  column_searchable_list=['username', 'email']
  column_filters=['username', 'email', 'funcao']
  column_editable_list=['username', 'email', 'funcao', 'active']
  create_modal=True
  edit_modal=True
  can_export=True
  column_sortable_list=['username']
  column_default_sort=('username', True)
  column_details_exclude_list=['password', 'recovery_code']
  column_export_exclude_list=['password', 'recovery_code']
  export_types=['json', 'yaml', 'csv', 'xls', 'df']

  def on_model_change(self, form, User, is_created):
    if 'password' in form:
      if form.password.data is not None:
        User.set_password(form.password.data)
      else:
        del form.password

class ProductView(ModelView):
  form_columns = ['usuario', 'categoria', 'name', 'description', 'qtd', 'image', 'price', 'date_created', 'last_update', 'status']