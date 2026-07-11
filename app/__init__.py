# -*- coding: utf-8 -*-
import os

from flask_admin import babel
from flask_bootstrap import Bootstrap

from config import config
from logging_config import logger
from flask import Flask, app, request, redirect, render_template

from app.extensions import db, migrate, babel
from app.model import *

from app.admin.Admin import start_views


def create_app():
    environment = os.getenv("FLASK_CONFIG", "development")

    app = Flask(__name__, template_folder=config[environment].TEMPLATE_FOLDER)
    

    app.config.from_object(config[environment])
    
    Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)
    
    start_views(app, db)
    
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        logger.info("========================================")
        logger.info("Inventory Management")
        logger.info(f"Configuration : {environment.title()}Config")
        logger.info(f"Environment   : {environment}")
        logger.info(f"Debug         : {app.config['DEBUG']}")
        logger.info(f"Testing       : {app.config['TESTING']}")
        logger.info(f"Host          : {app.config['HOST']}")
        logger.info(f"Port          : {app.config['PORT']}")
        logger.info("========================================")

    
    @app.route("/")
    def index():
        return f"Hello, World!"
    

    from app.routes import auth_bp, product_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)


    return app