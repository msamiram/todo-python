from app import create_app
from extensions import db
from models.user import User

app = create_app()

with app.app_context():
    users = User.query.all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Name: {user.first_name} {user.last_name}")
       

