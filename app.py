from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config, app_active
from admin.Admin import start_views

from controller.User import UserController

from extensions import db, migrate

def create_app(config_name=None):
  if config_name is None:
      config_name = app_active or 'development'
  
  app = Flask(__name__, template_folder='templates')
  app.config.from_object(app_config[config_name])
  app.secret_key = app.config['SECRET']

  db.init_app(app)

  start_views(app, db)

  # Import your models here
  from model import Role, User, Category, Product
  migrate.init_app(app, db)
  
  @app.route('/')
  def index():
    return 'Hello, world!'
  
  @app.route('/login/')
  def login():
    return f'Login here!'

  @app.route('/login/', methods=['POST'])
  def logi_post():
    user = UserController()
    email = request.form['email']
    password = request.form['password']

    result = user.login(email, password)

    if result:
      return redirect('/admin/')
    else:
      return render_template('login.html', 
                             data={'status': 401,
                                   'msg':'Incorrect data user',
                                   'type': None
                                   })
    
  @app.route('/recovery-password/')
  def recovery_password():
    return 'recovery password window here!'
  
  @app.route('/recovery-password/', methods=['POST'])
  def send_recovery_password():
    user = UserController()

    result = user.recovery(request.form['email'])

    if result:
      return render_template('recovery.html',data={'status': 200,'msg':'Recovery email sent successfully.'})
    else:
      return render_template('recovery.html',data={'status': 401,'msg':'Error sending recovery email.'})
  
  return app
