"""
Configuration classes for each application environment (development, testing, production).

The base class 'Config' provides shared settings. Each specific environment inherits and overrides as needed.
The attributes used in the configuration are:
  - CSRF_ENABLED: Enables protection against CSRF attacks in Flask sessions.
  - SECRET: A secret key used to generate encrypted tokens and secure data.
  - TEMPLATE_FOLDER: The path to the folder where HTML templates are stored.
  - ROOT_FOLDER: The path to the root of the project folder.
  - APP: A constant that can be used to store the Flask app instance.
  - SQLALCHEMY_DATABASE_URI: The connection string to connect to the MySQL database, using .env variables.
  - SQLALCHEMY_TRACK_MODIFICATIONS: Disables SQLAlchemy event notifications (recommended for performance).
  - TESTING: Enables or disables test mode.
  - DEBUG: Enables or disables debug mode (shows detailed errors when True).
  - IP_HOST: The IP address the server will run on.
  - PORT_HOST: The port the server will run on.
  - URL_MAIN: Full URL where the app will be available.
"""
"""
Environment selection:

To avoid manually setting the environment in the terminal, create a `.flaskenv` file
in the project root with the variable `FLASK_ENV`. This will be automatically loaded 
by python-dotenv.

Example .flaskenv content:
  FLASK_ENV=development

The variable `app_active` below reads the environment value and If no environment is provided, the default will be 'development'.
"""

import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
  CSRF_ENABLED = True
  SECRET= 'ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&' 
  TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')
  ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
  APP = None
  SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
  )
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
  TESTING = False 
  DEBUG = True
  IP_HOST = 'localhost'
  PORT_HOST = 8000
  URL_MAIN = f"http://{IP_HOST}:{PORT_HOST}"


class TestingConfig(Config):
  TESTING = True
  DEBUG = True
  IP_HOST = 'localhost'
  PORT_HOST = 5000
  URL_MAIN = f"http://{IP_HOST}:{PORT_HOST}"


class ProductionConfig(Config):
  TESTING = False 
  DEBUG = False
  IP_HOST = 'localhost'
  PORT_HOST = 8080
  URL_MAIN = f"http://{IP_HOST}:{PORT_HOST}"

app_config = {
  'development': DevelopmentConfig(),
  'testing': TestingConfig(),
  'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV', 'development') 