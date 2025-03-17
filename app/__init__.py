from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from app.extensions import db, ma, swagger
from app.routes import user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    ma.init_app(app)
    swagger.init_app(app)

    app.register_blueprint(user_blueprint)

    with app.app_context():
        db.create_all()

    return app
