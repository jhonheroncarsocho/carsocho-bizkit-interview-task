# search.py
from flask import Blueprint, request
from .model import Users

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    if bool(request.args.to_dict()):
        return search_users(request.args.to_dict()), 200
    else:
        return "ERROR: invalid request", 400


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    results=[]
    query = Users.query

    if "id" in args:
        query_id = query.filter(Users.id == args["id"])
        results = check_existence(results, query_id.all())

    if "name" in args:
        query_name = query.filter(Users.name.ilike(f"%{args['name']}%"))
        results = check_existence(results, query_name.all())

    if "age" in args:
        min_age = int(args["age"]) - 1
        max_age = int(args["age"]) + 1
        query_age = query.filter(Users.age.between(min_age, max_age))
        results = check_existence(results, query_age.all())

    if "occupation" in args:
        query_occu = query.filter(Users.occupation.ilike(f"%{args['occupation']}%"))
        results = check_existence(results, query_occu.all())

    return results

def check_existence(results, query_results):
    '''Check if the query results are already in the results list

    Parameters:
    -----------
        results: list
            a list of all queried User objects
        query_results: list
            a list of currently queried User objects

    Returns:
    --------
    list
        a list of dictionaries that are not already in the results list
    '''

    for user in query_results:
        current_user = {"id": user.id, "name": user.name, "age": user.age, "occupation": user.occupation}
        if current_user not in results:
            print(current_user)
            results.append(current_user)
        
    return results
