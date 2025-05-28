import os
import random, string

class Config(object):
  CSRF_ENABLED = True # Enable the use of encryption in flask sessions
  SECRETE = 'ysb_92=qe#' # It will be used at some point to create encrypted keys and values
  TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template") # default template path
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # Path to where the project root is located
  APP = None # Constant that will receive an application property

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