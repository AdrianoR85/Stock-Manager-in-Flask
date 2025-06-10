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

--- 
## Tecnologies
- Python
- Flask
- SQLAlchemy
- Migrate

---

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
- [ ] Configure Flask Database (SQL Alchemy).
- [ ] Run the Flask Application.

---

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

