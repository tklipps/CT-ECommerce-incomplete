from flask import Flask
from config import Config 
from flask_login import LoginManager 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 


login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in or register before shopping.'
login.login_message_category = "warning"

db = SQLAlchemy()

migrate = Migrate()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    



    return app
    

