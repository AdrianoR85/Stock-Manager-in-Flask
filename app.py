from flask import Flask, request, redirect, render_template
from config import app_active, app_config
from flask_sqlalchemy import SQLAlchemy
from admin.Admin import start_views

from controller.User import UserController

# Gets the active environment settings (development, test, or production)
config = app_config[app_active]

def create_app(config_name=None):
  if not config_name:
     config_name = 'development'
  # Creates the Flask app and sets the 'templates' folder
  app = Flask(__name__, template_folder='templates')

  # Loads all settings (DEBUG, SECRET_KEY, database URL, etc.)
  # from the chosen environment (development/test/production)
  app.config.from_object(app_config[config_name])


  # Initialize SQLAlchemy
  db = SQLAlchemy(config.APP)
  db.init_app(app)
  
  start_views(app,db)

  # Main route (home page)
  @app.route('/')
  def home():
      return 'Welcome to home page'
  
  @app.route('/login/')
  def login():
     return 'Here will enter the login screen'
  
  @app.route('/login', methods=['POST'])
  def login_post():
    user = UserController()

    email = request.form['email']
    password = request.form['password']

    result = user.login(email, password)

    if result:
      return redirect('/admin')
    else:
       return render_template('login.html', data={"status": 401,"msg": "User doesn't found", "type": None})

  @app.route('/recovery-password')
  def recovery_password():
     return 'Here will enter the recovery password screen'
  
  @app.route('/recovery-password', methods=['POST'])
  def send_recovery_password():
    user = UserController()
    result = user.recovery(request.form['email'])

    if result:
      return render_template("recovery.html", data={"status":201, "msg":"Recovery email sent succefully."})
    else:
      return render_template("recovery.html", data={"staus":401, "msg":"Erro sending recovery email."})

  @app.route('/profile', methods=['POST'])
  def create_profile():
    username = request.form['username']
    password = request.form['password']

    return f'This route has a post method e will create an user with the data; User:{username} and Password: {password}'

  @app.route('/profile/<int:id>', methods=['PUT'])
  def edit_total_profile(id):
    username = request.form['username']
    password = request.form['password']

    return f'This route has a PUT method e will edit the username to {username} and password to {password}'
  
  # Returns the configured app to use outside (e.g., in run.py)
  return app
