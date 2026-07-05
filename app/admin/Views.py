from app.extensions import ModelView
from flask_admin import AdminIndexView, expose
from app.controller import UserController, ProductController, CategoryController


class HomeView(AdminIndexView):
    extra_css = ["/static/css/home.css","https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

    
    @expose("/")
    def index(self):
        user_controller = UserController()
        category_controller = CategoryController()
        product_controller = ProductController()

        user = user_controller.total_users()
        category = category_controller.total_categories()   
        product = product_controller.total_products()

        return self.render("pages/home_admin.html",
                          report={
                            "users": 0 if user is None else user,
                            "categories": 0 if category is None else category,
                            "products": 0 if product is None else product
                          } 
                        )


class UserView(ModelView):
    # Rename the columns for display in the list view
    column_labels ={
        "funcao": "Função",
        "username": "Nome de Usuário",
        "email": "Email",
        "date_created": "Data de Criação",
        "last_updated": "Última Atualização",
        "active": "Ativo",
        "password": "Senha",
    }

    # Add a description for each column in the list view
    column_descriptions = {
        "funcao": "Função do usuário no sistema",
        "username": "Nome de usuário único",
        "email": "Endereço de email do usuário",
        "date_created": "Data em que o usuário foi criado",
        "last_updated": "Data da última atualização do usuário",
        "active": "Indica se o usuário está ativo ou não",
        "password": "Senha do usuário (não exibida por segurança)",
    }

    
    # Define the columns to be displayed in the list view
    column_exclude_list = ["password", "recovery_code"]
    form_excluded_columns = ["date_created","last_updated", "recovery_code"]

    # Define the form widget arguments for the password field
    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }

    # Customize the form fields for the User model
    can_set_page = True
    can_view_details = True
    column_searchable_list = ["username","email"]
    column_filters = ["username","email", "funcao"]
    column_editable_list = ["username","email", "funcao", "active"] 
    create_modal = True
    edit_modal = True
    can_export = True
    column_sortable_list = ["username"]
    column_default_sort = ("username", True)
    column_detail_exclude_list = ["password", "recovery_code"]
    column_export_exclude_list = ["password", "recovery_code"]
    export_types = ['csv', 'json', 'yaml', 'xls', 'xlsx']


    # Override the on_model_change method to handle password hashing
    def on_model_change(self, form, User, is_created):
        if "password" in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password