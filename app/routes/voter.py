from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect

from flask_login import login_required
from flask_login import current_user

from app.models import Candidate
from app.models import Vote

from app import db


voter_bp = Blueprint('voter', __name__)


# ================= DASHBOARD =================

@voter_bp.route('/dashboard')
@login_required
def dashboard():

    return render_template(
        'voter/dashboard.html',
        user=current_user
    )


# ================= CANDIDATES =================

@voter_bp.route('/candidates')
@login_required
def candidates():

    candidates = Candidate.query.all()

    return render_template(
        'voter/candidates.html',
        candidates=candidates
    )


# ================= VOTE PAGE =================

@voter_bp.route('/vote')
@login_required
def vote():

    candidates = Candidate.query.all()

    return render_template(
        'voter/vote.html',
        candidates=candidates
    )


# ================= CAST VOTE =================

@voter_bp.route('/cast-vote', methods=['POST'])
@login_required
def cast_vote():

    if current_user.has_voted:

        return jsonify({
            'error': 'You already voted'
        }), 400

    data = request.get_json()

    candidate_id = data.get('candidate_id')

    candidate = Candidate.query.get(candidate_id)

    if not candidate:

        return jsonify({
            'error': 'Candidate not found'
        }), 404

    vote = Vote(

        voter_id=current_user.id,

        candidate_id=candidate_id

    )

    db.session.add(vote)

    current_user.has_voted = True

    db.session.commit()

    return jsonify({
        'message': 'Vote successful'
    })


# ================= MY RESULT =================

@voter_bp.route('/myresult')
@login_required
def myresult():

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
        'voter/myresult.html',
        results=results
    )


# ================= CONFIRMATION =================

@voter_bp.route('/confirmation')
@login_required
def confirmation():

    return render_template(
        'voter/confirmation.html'
    )