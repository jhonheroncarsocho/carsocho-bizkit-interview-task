from flask import Blueprint, jsonify

from .model import Users, Friends, db


bp = Blueprint("view_friend_request", __name__, url_prefix="/view_friend_request")

@bp.route("", methods=["GET"])
def view_friend_request():
    return jsonify(get_friend_request()), 200

def get_friend_request():
    '''Get all the the friend requests from friends table
    
    Returns:
    --------
    list
        list of dictiorany containing the following parameters:
            id: string
                primary key of the user table
            name: string
                name of the user
            age: integer
                age of the user
            occupation: string
                occupation of the user
            request_id: string
                primary key of the friends table
    '''
    user_query = Users.query.join(Friends, Users.id == Friends.from_user_id).add_column(Friends.id)\
        .filter(Friends.status == "pending").all()

    return [{"id": user[0].id, "name": user[0].name, "age": user[0].age, "occupation": user[0].occupation, "request_id": user[1]}\
             for user in user_query]
