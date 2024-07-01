from flask import Blueprint, request, jsonify
from .model import Users, db

bp = Blueprint("add_user", __name__, url_prefix="/add_user")

@bp.route("", methods=["POST"])
def add_user():
    """Create a new phasebook account"""
    try:
        db.session.add(Users(name=request.form["name"],
                             age=request.form["age"],
                             occupation=request.form["occupation"]))
        db.session.commit()

        return f"You have successfully created an account.", 201
    
    except Exception as e:
        return f"Error: {e}", 400