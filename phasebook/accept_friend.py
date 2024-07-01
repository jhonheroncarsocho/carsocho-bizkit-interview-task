from flask import Blueprint, request, jsonify
from .model import Users, Friends, db

bp = Blueprint("accept_friend", __name__, url_prefix="/accept_friend")

@bp.route("/<int:request_id>", methods=["PUT"])
def accept_friend(request_id):
    response, status = accept_users(request_id)
    return jsonify(response), status

def accept_users(request_id):
    '''Accept friends

    Parameters:
    -----------
        request_id: int
            the id of the friend request

    Returns:
    -----------
       tuple
            a dictionary of accepted friend containing the following parameters:
                id: string
                    primary key of the users table
                name: string
                    name of the user
                age: integer
                    age of the user
                occupation: string
                    occupation of the user
            and HTTP status code
    '''

    try:
        # Retrieve the friend request
        friend_request = Friends.query.get_or_404(request_id)
        
        # Assuming 'sender_id' is the ID of the user who sent the friend request
        user_id = friend_request.from_user_id
        
        # Retrieve user details
        user = Users.query.get_or_404(user_id)
        
        # Update the friend request status
        friend_request.status = "accepted"
        db.session.commit()
        
        # Prepare the response dictionary
        response = {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "occupation": user.occupation
        }
        
        return response, 200
    
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 404
