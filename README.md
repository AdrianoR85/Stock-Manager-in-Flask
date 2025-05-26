# Stock Manager in Flask
This repository is for my learning with Flask. I will use the book Flask de A a Z to study, where the author teaches Flask by developing a stock manager. Everything I learn on this path will be added here.

## About the Project
"You will make a product management system. In this system, we will organize categories, users, and roles. You can limit a user to access only the system API or also the admin area, with secure login."

## Project Structure
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