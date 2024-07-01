from flask import Blueprint, jsonify
from .model import Users, Friends

bp = Blueprint("view_friends", __name__, url_prefix="/view_friends")

@bp.route("")
def view_friends():
    user_query = Users.query.join(Friends, Users.id == Friends.from_user_id)\
        .filter(Friends.status == "accepted").all()
    
    if not bool(user_query):
        return "You have no friend"
    else:
        users = [{"id":user.id,  "name":user.name, "age":user.age, "occupation":user.occupation} for user in user_query]
        return jsonify(users), 200