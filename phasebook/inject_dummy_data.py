from flask import current_app
from .model import Users, db
from faker import Faker


def add_dummy_data():
    """Generate and add dummy user data for users table"""
    fake = Faker()
    with current_app.app_context():
        # Create some dummy data
        dummy_users = []
        for _ in range(500):
            user = Users(
                name=fake.name(),
                age=fake.random_int(min=18, max=80),
                occupation=fake.job()
            )
            dummy_users.append(user)
        
        # Add the dummy data to the session and commit
        db.session.bulk_save_objects(dummy_users)
        db.session.commit()
        print('Dummy data added successfully.')
