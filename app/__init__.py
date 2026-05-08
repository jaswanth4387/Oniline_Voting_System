from flask import Flask

from config import Config

from app.extensions import (
    db,
    login_manager,
    migrate
)


# ================= CREATE APP =================

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)


    # ================= INITIALIZE EXTENSIONS =================

    db.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app, db)


    # ================= LOGIN SETTINGS =================

    login_manager.login_view = 'auth.login'


    # ================= IMPORT MODELS =================

    from app.models import (
        User,
        Candidate,
        Vote,
        Election,
        VoterApplication
    )


    # ================= USER LOADER =================

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(
            int(user_id)
        )


    # ================= REGISTER BLUEPRINTS =================

    from app.routes.public import public_bp
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.voter import voter_bp


    app.register_blueprint(
        public_bp
    )

    app.register_blueprint(
        auth_bp
    )

    app.register_blueprint(
        admin_bp
    )

    app.register_blueprint(
        voter_bp
    )


    return app