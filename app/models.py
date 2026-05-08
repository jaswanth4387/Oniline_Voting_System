from app.extensions import db

from flask_login import UserMixin

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


# ================= USERS =================

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100))

    email = db.Column(
        db.String(120),
        unique=True
    )

    voter_id = db.Column(
        db.String(50),
        unique=True
    )

    password_hash = db.Column(db.String(255))

    has_voted = db.Column(
        db.Boolean,
        default=False
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    def set_password(self, password):

        self.password_hash = generate_password_hash(
            password
        )

    def check_password(self, password):

        return check_password_hash(
            self.password_hash,
            password
        )


# ================= CANDIDATES =================

class Candidate(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    party = db.Column(db.String(100))

    constituency = db.Column(db.String(100))

    photo = db.Column(db.String(255))

    symbol = db.Column(db.String(255))


# ================= VOTES =================

class Vote(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    voter_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )

    candidate_id = db.Column(
        db.Integer,
        db.ForeignKey('candidate.id')
    )


# ================= NEW VOTER APPLICATION =================

class VoterApplication(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name = db.Column(
        db.String(100)
    )

    parent_name = db.Column(
        db.String(100)
    )

    dob = db.Column(
        db.String(20)
    )

    gender = db.Column(
        db.String(20)
    )

    mobile = db.Column(
        db.String(15)
    )

    email = db.Column(
        db.String(120)
    )

    aadhaar = db.Column(
        db.String(20)
    )

    caste = db.Column(
        db.String(50)
    )

    address = db.Column(
        db.Text
    )

    district = db.Column(
        db.String(100)
    )

    state = db.Column(
        db.String(100)
    )

    pincode = db.Column(
        db.String(10)
    )

    assembly = db.Column(
        db.String(100)
    )

    parliament = db.Column(
        db.String(100)
    )

    photo = db.Column(
        db.String(255)
    )

    aadhaar_file = db.Column(
        db.String(255)
    )

    address_proof = db.Column(
        db.String(255)
    )

    # ================= STATUS =================

    status = db.Column(

        db.String(50),

        default='PENDING'

    )

    document_verified = db.Column(

        db.Boolean,

        default=False

    )

    field_verified = db.Column(

        db.Boolean,

        default=False

    )
    status = db.Column(
    db.String(50),
    default='PENDING'
    )
    
    tracking_id = db.Column(
    db.String(30),
    unique=True
    )

class Election(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    start_date = db.Column(
        db.DateTime
    )

    end_date = db.Column(
        db.DateTime
    )