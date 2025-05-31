import os
import random, string
from dotenv import load_dotenv

load_dotenv()

class Config(object):
  CSRF_ENABLED = True # Enable the use of encryption in flask sessions
  SECRET = 'ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&' # It will be used at some point to create encrypted keys and values
  TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates") # default template path
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # Path to where the project root is located
  APP = None # Constant that will receive an application property
  SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

class DevelopmentConfig(Config):
  TESTING = True
  DEBUG = True
  IP_HOST = 'localhost'
  PORT_HOST = 8000
  URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


class TestingConfig(Config):
  TESTING = True
  DEBUG = True
  IP_HOST =  'localhost' # Usually, there is an IP of a cloud server here, not the localhost address
  PORT_HOST = 5000
  URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


class ProductionConfig(Config):
  TESTING = False
  DEBUG = False
  IP_HOST =  'localhost' # Usually, there is an IP of a cloud server here, not the localhost address
  PORT_HOST = 8080
  URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

app_config = {
  'development': DevelopmentConfig(),
  'testing': TestingConfig(),
  'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')