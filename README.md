# 🛠 Stock Manager in Flask

[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()

This project is based on the book *"Flask from A to Z – Build More Complete Web Applications"*, written by **Tiago Luiz**. The book teaches how to build web applications using **Flask**, a popular Python web framework.

The goal of the book is to help the reader go from basic to advanced levels in web development with Flask. It covers many important topics
The final result is a complete and functional web app, ready for real use. 

The book also shows good practices for writing clean and easy-to-maintain code.
This project follows the book's content, with notes, example code, and some possible changes or improvements.

[Link to buy the book](https://www.casadocodigo.com.br/products/livro-flask-a-z)

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
-----------------------------------------------

## Tecnologies
- Python
- Flask
- SQLAlchemy
- Migrate

-----------------------------------------------

 ## Required Libraries
- **```pip install Flask```**: A small web framework to build websites and APIs.
- **```pip install Flask-SQLAlchemy```**: A tool to help Python talk to databases using objects
- **```pip install Flask-Admin```**: A tool to create an admin panel for your Flask app
- **```pip install pymysql```**: A library that lets Python connect to a MySQL database.
- **```pip install Flask-Migrate```**: Helps manage changes in the database using Alembic.
- **```pip install passlib```**: A library to hash (encrypt) passwords safely.

## 🛠️ Steps

### Step 1 - Getting Started

- [x] Creating the Structure.
- [x] Install the required libraries.
- [x] Create environments for each phase of the project.
- [x] Create a Flask Application.
- [x] Configure Flask Database (SQL Alchemy).
- [x] Run the Flask Application.

### Step 2 -  Database Setup
#### Models:
- [ ] Create User Mode
- [ ] Create Role Model
- [ ] Create Category Model
- [ ] Create Product Model

#### Migrations
- [ ] Initialize Migration System (`flask db init`)
- [ ] Generate Migration Script (`flask db migrate -m "Initial models"`)
- [ ] Apply Migrations to Database (`flask db upgrade`)

-----------------------------------------------

## About flask
Flask is a lightweight and easy-to-use web framework for Python. It is designed to help developers build web applications quickly and with minimal code. Flask is called a "micro" framework because it provides only the essential tools needed for web development, such as routing (handling URLs), request handling, and template rendering. However, it can be extended with additional libraries for more complex features like databases or user authentication.

*Example of a Simple Flask App:*
```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello, Flask!"

    if __name__ == '__main__':
        app.run(debug=True)
```
#### Key Features of Flask:
- *Simple and Flexible* – Flask is easy to learn and allows developers to choose how they want to structure their - applications.
- *Built-in Development Server* – It comes with a server for testing, making it convenient during development.
- *Routing* – You can define different URLs and connect them to Python functions.
- *Templates* – Flask supports Jinja2, a powerful template engine to create dynamic HTML pages.
- *Extensible* – You can add plugins for databases (like SQLite or PostgreSQL), forms, security, and more. 

-----------------------------------------------
## About SQLAlchemy and Models

**SQLAlchemy** is a popular Python library for working with databases. It provides tools to interact with relational databases (like MySQL, PostgreSQL, SQLite) in an efficient and Pythonic way.

**Models** are Python classes that represent database tables. They define the structure of your data and allow you to interact with the database in an object-oriented way.

#### Key Features of SQLAlchemy
- *ORM (Object-Relational Mapping)* – Instead of writing raw SQL, you can work with Python classes and objects.
- *SQL Expression Language* – Allows writing SQL queries in a Python-friendly way.
- *Database Agnostic* – Works with different database systems (SQLite, PostgreSQL, MySQL, etc.) without changing much code.
- *Session Management* – Helps manage database transactions safely.
- *Integration with Flask* – Often used with Flask in web applications (e.g., Flask-SQLAlchemy).

#### Example
```python
rom flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # SQLite database
db = SQLAlchemy(app)

# Define a Model (Python class for a database table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
db.create_all()

# Add a new user
new_user = User(username='john', email='john@example.com')
db.session.add(new_user)
db.session.commit()

# Query all users
users = User.query.all()
print(users)  # Output: [<User john>]
```
-----------------------------------------------

## 🔄 Database Migration Workflow (Flask-Migrate)

Flask-Migrate uses Alembic to handle SQLAlchemy database migrations. Follow the steps below to set up and manage database schema changes.

### ✅ Initial Setup (Only Once)
If this is your first time setting up migrations:

```bash
flask db init
```
This will create a migrations/ directory with the necessary Alembic configuration files.

### 🛠 Apply Model Changes
Whenever you make changes to your models (add tables, modify fields, etc.), follow this process:

1. Generate a new migration script:

```bash
  flask db migrate -m "Describe the change, e.g., add user table"
```
2. Apply the migration to the database:

```bash
  flask db upgrade
```
This will apply the changes to your database schema.

### 🔁 Repeat as Needed
Every time you update your models:
- Run `flask db migrate` to create a new migration file
- Then run `flask db upgrade` to apply it

### ⚠️ Important Notes
Make sure all models are imported before calling `migrate.init_app(app, db)` inside your create_app function.

Example:

```python
  db.init_app(app)
  from model import Role, User, Category, Product  # import models here
  migrate.init_app(app, db)
```
Ensure the `model/ directory has an __init__.py` file so Python recognizes it as a package.

