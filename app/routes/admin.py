from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from werkzeug.security import check_password_hash

from app.models import User
from app.models import VoterApplication

from app.extensions import db


admin_bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin'
)


# ================= ADMIN LOGIN =================

@admin_bp.route(
    '/login',
    methods=['GET', 'POST']
)
def login():

    if request.method == 'POST':

        email = request.form.get(
            'email'
        )

        password = request.form.get(
            'password'
        )

        admin = User.query.filter_by(
            email=email,
            is_admin=True
        ).first()


        if admin and check_password_hash(
            admin.password_hash,
            password
        ):

            login_user(admin)

            return redirect(
                '/admin/dashboard'
            )

        else:

            flash(
                'Invalid admin credentials'
            )


    return render_template(
        'admin/login.html'
    )


# ================= ADMIN DASHBOARD =================

@admin_bp.route('/dashboard')
@login_required
def dashboard():

    applications = (
        VoterApplication.query
        .order_by(
            VoterApplication.id.desc()
        )
        .all()
    )

    return render_template(
        'admin/dashboard.html',
        applications=applications
    )


# ================= APPROVE =================

@admin_bp.route(
    '/approve/<int:id>'
)
@login_required
def approve_application(id):

    application = (
        VoterApplication.query
        .get_or_404(id)
    )

    application.status = 'APPROVED'

    db.session.commit()

    flash(
        'Application Approved'
    )

    return redirect(
        '/admin/dashboard'
    )


# ================= REJECT =================

@admin_bp.route(
    '/reject/<int:id>'
)
@login_required
def reject_application(id):

    application = (
        VoterApplication.query
        .get_or_404(id)
    )

    application.status = 'REJECTED'

    db.session.commit()

    flash(
        'Application Rejected'
    )

    return redirect(
        '/admin/dashboard'
    )


# ================= LOGOUT =================

@admin_bp.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(
        '/admin/login'
    )