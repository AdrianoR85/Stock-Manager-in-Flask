import os 
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    TEMPLATE_FOLDER = BASE_DIR / "templates"
    ROOT_DIR = BASE_DIR

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

    HOST = "127.0.0.1"
    PORT = 8000

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@127.0.0.1/development"
    )


class TestingConfig(Config):
    DEBUG = False
    TESTING = True

    HOST = "127.0.0.1"
    PORT = 5000

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@127.0.0.1/testing"
    )


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

    HOST = "0.0.0.0"
    PORT = 8080

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@127.0.0.1/inventory_management"
    )


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}