from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

from flask_login import login_user
from flask_login import login_required
from flask_login import current_user

from app.models import User
from app.models import Candidate
from app.models import Vote

from app.extensions import db


admin_bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin'
)


# ================= ADMIN LOGIN =================

@admin_bp.route('/login', methods=['GET', 'POST'])
def admin_login():

    if request.method == 'POST':

        email = request.form.get('email')

        password = request.form.get('password')

        admin = User.query.filter_by(
            email=email,
            is_admin=True
        ).first()

        if admin and admin.check_password(password):

            login_user(admin)

            return redirect('/admin/dashboard')

        flash('Invalid admin credentials')

    return render_template(
        'admin/login.html'
    )


# ================= ADMIN ACCESS CHECK =================

def admin_required():

    if not current_user.is_authenticated:

        return False

    if not current_user.is_admin:

        return False

    return True


# ================= DASHBOARD =================

@admin_bp.route('/dashboard')
@login_required
def dashboard():

    if not admin_required():

        return redirect('/login')

    total_voters = User.query.count()

    total_candidates = Candidate.query.count()

    total_votes = Vote.query.count()

    return render_template(

        'admin/dashboard.html',

        total_voters=total_voters,

        total_candidates=total_candidates,

        total_votes=total_votes
    )


# ================= CANDIDATES =================

@admin_bp.route('/candidates')
@login_required
def candidates():

    if not admin_required():

        return redirect('/login')

    candidates = Candidate.query.all()

    return render_template(

        'admin/candidates.html',

        candidates=candidates
    )


# ================= ADD CANDIDATE =================

@admin_bp.route(
    '/add-candidate',
    methods=['GET', 'POST']
)
@login_required
def add_candidate():

    if not admin_required():

        return redirect('/login')

    if request.method == 'POST':

        candidate = Candidate(

            name=request.form.get('name'),

            party=request.form.get('party'),

            constituency=request.form.get(
                'constituency'
            ),

            photo=request.form.get('photo'),

            symbol=request.form.get('symbol')

        )

        db.session.add(candidate)

        db.session.commit()

        flash('Candidate added successfully')

        return redirect('/admin/candidates')

    return render_template(
        'admin/add_candidate.html'
    )


# ================= DELETE CANDIDATE =================

@admin_bp.route('/delete-candidate/<int:id>')
@login_required
def delete_candidate(id):

    if not admin_required():

        return redirect('/login')

    candidate = Candidate.query.get(id)

    if candidate:

        db.session.delete(candidate)

        db.session.commit()

        flash('Candidate deleted')

    return redirect('/admin/candidates')


# ================= RESULTS =================

@admin_bp.route('/results')
@login_required
def results():

    if not admin_required():

        return redirect('/login')

    votes = Vote.query.all()

    results = {}

    for vote in votes:

        candidate = Candidate.query.get(
            vote.candidate_id
        )

        if candidate.name in results:

            results[candidate.name] += 1

        else:

            results[candidate.name] = 1

    return render_template(

        'admin/results.html',

        results=results
    )


# ================= VOTERS =================

@admin_bp.route('/voters')
@login_required
def voters():

    if not admin_required():

        return redirect('/login')

    voters = User.query.filter_by(
        is_admin=False
    ).all()

    return render_template(

        'admin/voters.html',

        voters=voters
    )