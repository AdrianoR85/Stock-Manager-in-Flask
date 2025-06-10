from flask import Flask
from config import app_active, app_config
import os 

from flask import Flask
from config import app_active, app_config
import os 

# Gets the active environment settings (development, test, or production)
config = app_config[app_active]

def create_app(config_name):
  # Creates the Flask app and sets the 'templates' folder
  app = Flask(__name__, template_folder='templates')

  # Loads all settings (DEBUG, SECRET_KEY, database URL, etc.)
  # from the chosen environment (development/test/production)
  app.config.from_object(app_config[config_name])

  # Main route (home page)
  @app.route('/')
  def home():
      return 'Welcome to home page'

  # Returns the configured app to use outside (e.g., in run.py)
  return app
