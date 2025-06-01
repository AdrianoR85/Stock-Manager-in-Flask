from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config, app_active

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
  if config_name is None:
      config_name = app_active or 'development'
  
  app = Flask(__name__, template_folder='template')
  app.config.from_object(app_config[config_name])
  app.secret_key = app.config['SECRET']

  db.init_app(app)

  # Import your models here
  from model import Role, User, Category, Product

  migrate.init_app(app, db)
  
  @app.route('/')
  def index():
    return 'Hello, world!'
  
  return app
