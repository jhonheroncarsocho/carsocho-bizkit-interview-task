from flask import Blueprint, jsonify
from .model import Users, Friends, db

bp = Blueprint("unfriend", __name__, url_prefix="/unfriend")

@bp.route("/<int:user_id>", methods=["DELETE"])
def unfriend(user_id):
    '''Unfriend a user

    Parameters:
    -----------
        user_id: int
            the id of the user to unfriend

    Returns:
    --------
        A success message that a user has been unfriended
    '''
    try:
        # Find the friendship record
        friendship = Friends.query.filter_by(from_user_id=user_id, status="accepted").first()
        if not friendship:
            return jsonify({"error": "Friendship not found"}), 404

        # Find the user record
        user = Users.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Delete the friendship record
        db.session.delete(friendship)
        db.session.commit()

        return jsonify({"message": f"{user.name} unfriended successfully."}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
