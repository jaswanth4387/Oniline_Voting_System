from flask import Flask

from app.extensions import db
from app.extensions import migrate
from app.extensions import login_manager

from app.models import User

from config import Config


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'


    # ================= USER LOADER =================

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))


    # ================= BLUEPRINTS =================

    from app.routes.public import public_bp
    from app.routes.auth import auth_bp
    from app.routes.voter import voter_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(public_bp)

    app.register_blueprint(auth_bp)

    app.register_blueprint(voter_bp)

    app.register_blueprint(admin_bp)

    return app