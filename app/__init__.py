import os
from flask import Flask
from .extensions import db, login_manager, bcrypt
from config import Config
from flask_cors import CORS

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))

    template_dir = os.path.join(base_dir, "..", "templates")
    static_dir = os.path.join(base_dir, "..", "static")

    app = Flask(__name__,
                template_folder=template_dir,
                static_folder=static_dir)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from .routes.auth import auth_bp
    from .routes.opportunity import opp_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(opp_bp)

    return app

