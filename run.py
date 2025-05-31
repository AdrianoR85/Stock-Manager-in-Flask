"""
This file creates the application runtime configuration based on the app and config files.
"""
import sys 
from importlib import reload

from app import create_app
from config import app_active, app_config

config = app_config[app_active] # Getting an instance (object) of the configuration environment
config.APP = create_app(app_active)

if __name__ == "__main__":
  config.APP.run(
    host=config.IP_HOST,
    port=config.PORT_HOST
  )
  reload(sys)