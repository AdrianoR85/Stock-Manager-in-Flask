from importlib import reload
import sys
from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(
        host=app.config.get("HOST"),
        port=app.config.get("PORT"),
        debug=app.config.get("DEBUG")
    )
    
    reload(sys)