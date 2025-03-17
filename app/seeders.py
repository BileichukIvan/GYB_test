from app.models import User
from app.extensions import db


def seed_users():

    seed_data = [
        User(name="John Deer1", email="johndeer1@email.com"),
        User(name="John Deer2", email="johndeer2@email.com"),
        User(name="John Deer3", email="johndeer3@email.com"),
        User(name="John Deer4", email="johndeer4@email.com"),
    ]

    db.session.bulk_save_objects(seed_data)
    db.session.commit()
    print("Seeding users successfully")
