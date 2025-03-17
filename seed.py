from app.seeders import seed_users
from run import app

with app.app_context():
    seed_users()
