from flask import Flask
from flask_wtf.csrf import CSRFProtect
from topsecret.migrations import create_db, migrate
from decouple import config
from wtforms.csrf.core import CSRF

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.secret_key = config("SECRET_KEY")

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    from topsecret.models import db, Users

    url = create_db()

    app.config['SQLALCHEMY_DATABASE_URI'] = str(url)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    migrate.init_app(app, db)

    from topsecret.routes.main import main, page_not_found

    with app.app_context():
        db.drop_all() # clear db
        db.create_all() # create db

    app.register_blueprint(main)
    app.register_error_handler(404, page_not_found)

    return app