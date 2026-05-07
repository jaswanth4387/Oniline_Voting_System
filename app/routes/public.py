from flask import Blueprint
from flask import render_template

public_bp = Blueprint('public', __name__)


# ================= HOME =================

@public_bp.route('/')
def home():

    return render_template(
        'public/index.html'
    )


# ================= ABOUT =================

@public_bp.route('/about')
def about():

    return render_template(
        'public/about.html'
    )


# ================= NOTICES =================

@public_bp.route('/notices')
def notices():

    return render_template(
        'public/notices.html'
    )


# ================= NOTICES 2 =================

@public_bp.route('/notices2')
def notices2():

    return render_template(
        'public/notices2.html'
    )


# ================= FORMS =================

@public_bp.route('/forms')
def forms():

    return render_template(
        'public/forms.html'
    )


# ================= COMPLAINT =================

@public_bp.route('/complaint')
def complaint():

    return render_template(
        'public/complaint.html'
    )


# ================= RESULTS =================

@public_bp.route('/results')
def results():

    return render_template(
        'public/results.html'
    )