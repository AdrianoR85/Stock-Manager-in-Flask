# 🛠 Stock Manager in Flask

[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()

This repository is for my learning with Flask. I will use the book Flask de A a Z to study, where the author teaches Flask by developing a stock manager. Everything I learn on this path will be added here.

## About the Project
"You will make a product management system. In this system, we will organize categories, users, and roles. You can limit a user to access only the system API or also the admin area, with secure login."

## 📁 Project Structure
```bash
stock-manager-flask
| app.py
| config.py
| migrate.py
| run.py
| 
|__admin
|  | Admin.py
|  | Views.py 
|
|__model
|  | Category.py
|  | Product.py 
|  | User.py
|  | Role.py
|
|__controller
|  | Email.py
|  | Product.py 
|  | User.py
|  
|__static
|  | login.css
|  | home.css 
|  
|__template
|  | login.html
|  | home_admin.html 
|  | lnew_password.html
|  | recovery.html
```

--- 
## Tecnologies
- Python
- Flask
- SQLAlchemy

## 🛠️ What Was Done

### config.py
- Created a base configuration class called `Config` with shared attributes.
- Defined specific classes for:
  - Development: `DevelopmentConfig`
  - Testing: `TestingConfig`
  - Production: `ProductionConfig`
- Used class inheritance to avoid code duplication and maintain organized settings.
- Mapped the configurations using the environment variable `FLASK_ENV`.

### app.py
- Retrieved the active configuration object based on the current environment using `config = app_config[app_active]`
- Defined the factory function `create_app(config_name)` to create and configure a Flask application instance dynamically.
- Inside create_app:
  - Created a new Flask app, specifying `'templates'` as the folder for HTML templates.
  - Set the app's secret key from the configuration object `(config.SECRET)`.
  - Loaded the configuration from the configuration class mapped by `config_name` with `app.config.from_object()`.
  - Loaded additional configuration from the config.py file using `app.config.from_pyfile()`.
  - Defined a basic route `'/'` that returns `'Hello, world!'` when accessed.
- Creates the database instance.
- Initializes SQLAlchemy with the app.
- Returned the fully configured Flask application instance from the factory function.

### run.py
- Imported `create_app` and configuration data to set up the app environment.
- Selected the active configuration instance based on the `FLASK_ENV variable`.
- Created the Flask app and stored it inside the configuration object (`config.APP`).
- Started the Flask server using host and port values from the active configuration.