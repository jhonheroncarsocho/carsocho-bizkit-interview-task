from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


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

    get_search_param = [key for key in args]
    
    if get_search_param:
        results = []
        for param in get_search_param:
            if param == "id":
                for user in USERS:
                    if args[param] in user[param]:
                        if user not in results:
                            results.append(user)
                
            if param == "name":
                for user in USERS:
                    if partially_matched(user[param], args[param]):
                        if user not in results:
                            results.append(user)

            if param == "age":
                min_age = int(args[param]) - 1
                max_age = int(args[param]) + 1
                for user in USERS:
                    if min_age <= user[param] <= max_age:
                        if user not in results:
                            results.append(user)
            
            if param == "occupation":
                for user in USERS:
                    if partially_matched(user[param], args[param]):
                        if user not in results:
                            results.append(user)

        # results = sorted(results, key=lambda i: i['id'])
        return results
    else:
        return USERS

def partially_matched(user_param, args_param):
    """
    Check if user_param and args_param is partial, case-insensitive match
    
    Parameters:
        user_param (str): String value of user[param] that is to match to args[param]
        args_param (str): String value of args[param] that is to match to user[param]
    
    Returns:
        boolean: True if user_param and args_param is partial, case-insensitive match, False otherwise"""
    
    return user_param.lower().find(args_param.lower()) != -1
