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
- Migrate

---

 ## Required Libraries
- **Flask:** A small web framework to build websites and APIs.
- **SQL Alchemy:** A tool to help Python talk to databases using objects
- **Flask-Admin:** A tool to create an admin panel for your Flask app
- **PyMySQ:** A library that lets Python connect to a MySQL database.
- **Flask-Migrate:** Helps manage changes in the database using Alembic.
- **passlib:** A library to hash (encrypt) passwords safely.

## 🛠️ Steps

### Step 1 - Getting Started

- [x] Creating the Structure.
- [x] Install the required libraries.
  - ```pip install Flask```
  - ```pip install Flask-SQLAlchemy```
  - ```pip install Flask-Admin```
  - ```pip install Flask-Migrate```
  - ```pip install pymysql```
  - ```pip install passlib```
- [ ] Create environments for each phase of the project.
- [ ] Create a Flask Application.v	No
- [ ] Configure Flask Database (SQL Alchemy + Migrate).
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

