from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink


db = SQLAlchemy()
migrate = Migrate()
babel = Babel()