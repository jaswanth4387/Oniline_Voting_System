from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
import random

from app.models import VoterApplication
from app.extensions import db


public_bp = Blueprint(
    'public',
    __name__
)


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


# ================= NEW VOTER REGISTRATION =================

@public_bp.route(
    '/new-voter-registration',
    methods=['GET', 'POST']
)
def new_voter_registration():

    if request.method == 'POST':

        # ================= TRACKING ID =================

        tracking_id = (
            "TMP" +
            str(
                random.randint(
                    100000000,
                    999999999
                )
            )
        )


        # ================= CREATE APPLICATION =================

        application = VoterApplication(

            # PERSONAL

            full_name=(
                request.form.get(
                    'first_name'
                ) + " " +
                request.form.get(
                    'last_name'
                )
            ),

            parent_name=request.form.get(
                'father_name'
            ),

            dob=request.form.get(
                'dob'
            ),

            gender=request.form.get(
                'gender'
            ),

            caste=request.form.get(
                'caste'
            ),


            # CONTACT

            mobile=request.form.get(
                'mobile'
            ),

            email=request.form.get(
                'email'
            ),


            # IDENTITY

            aadhaar=request.form.get(
                'aadhaar'
            ),


            # ADDRESS

            address=request.form.get(
                'address'
            ),

            district=request.form.get(
                'district'
            ),

            state=request.form.get(
                'state'
            ),

            pincode=request.form.get(
                'pincode'
            ),

            assembly=request.form.get(
                'assembly'
            ),

            parliament=request.form.get(
                'parliament'
            ),


            # STATUS

            status='PENDING',

            document_verified=False,

            field_verified=False,

            tracking_id=tracking_id

        )


        # ================= SAVE TO DATABASE =================

        db.session.add(application)

        db.session.commit()


        # ================= SUCCESS PAGE =================

        return render_template(
            'public/application_success.html',
            tracking_id=tracking_id
        )


    return render_template(
        'public/new_voter_registration.html'
    )