from app.extensions import ModelView

class UserView(ModelView):
    column_exclude_list = ["password", "recovery_code"]
    form_excluded_columns = ["date_created","last_updated", "recovery_code"]

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }

    def on_model_change(self, form, User, is_created):
        if "password" in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password