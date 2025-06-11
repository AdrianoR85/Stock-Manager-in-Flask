from app import create_app
from config import app_active, app_config
from flask_sqlalchemy import SQLAlchemy

# Load the correct config (development/test/production) 
config = app_config[app_active]

# Create the Flask app and save it in config.APP
config.APP = create_app(app_active)

# Run the app only if this file is executed directly
if __name__ == "__main__":
  # Start the server with custom host and port from config
  config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
