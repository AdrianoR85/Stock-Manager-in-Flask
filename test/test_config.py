import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import app_active, app_config

config = app_config[app_active]

print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(f"Active environment: {app_active}")
print(f"DEBUG: {config.DEBUG}")
print(f"TESTING: {config.TESTING}")
print(f"DATABASE URI: {config.SQLALCHEMY_DATABASE_URI}")
print(f"URL_MAIN: {config.URL_MAIN}")
print(f"TEMPLATE_FOLDER: {config.TEMPLATE_FOLDER}")