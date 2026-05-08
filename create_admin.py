from app import create_app

from app.extensions import db

from app.models import User

from werkzeug.security import (
    generate_password_hash
)


app = create_app()


with app.app_context():

    existing_admin = User.query.filter_by(
        email='admin@gmail.com'
    ).first()


    if existing_admin:

        print(
            "Admin already exists"
        )

    else:

        admin = User(

            full_name='System Admin',

            email='admin@gmail.com',

            voter_id='ADMIN001',

            password_hash=generate_password_hash(
                'admin123'
            ),

            is_admin=True

        )


        db.session.add(admin)

        db.session.commit()


        print(
            "Admin Created Successfully"
        )