from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from app.models import User
from app import db


auth_bp = Blueprint('auth', __name__)


# ================= LOGIN =================

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        voter_id = request.form.get('voter_id')

        password = request.form.get('password')

        user = User.query.filter_by(
            voter_id=voter_id
        ).first()

        if user and user.check_password(password):

            login_user(user)

            # ADMIN LOGIN
            if user.is_admin:

                return redirect('/admin/dashboard')

            # NORMAL USER
            return redirect('/dashboard')

        flash('Invalid credentials')

    return render_template(
        'auth/login.html'
    )


# ================= SIGNUP =================

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        full_name = request.form.get('full_name')

        email = request.form.get('email')

        voter_id = request.form.get('voter_id')

        password = request.form.get('password')

        existing_user = User.query.filter_by(
            voter_id=voter_id
        ).first()

        if existing_user:

            flash('Voter ID already exists')

            return redirect('/signup')

        user = User(

            full_name=full_name,

            email=email,

            voter_id=voter_id

        )

        user.set_password(password)

        db.session.add(user)

        db.session.commit()

        flash('Registration successful')

        return redirect('/login')

    return render_template(
        'auth/signup.html'
    )


# ================= LOGOUT =================

@auth_bp.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect('/')