from flask_jwt_extended import get_jwt_identity
from models.user import User

def get_current_user():
    user_id = get_jwt_identity()
    return User.query.get(int(user_id))
