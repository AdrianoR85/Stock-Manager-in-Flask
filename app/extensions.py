from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()