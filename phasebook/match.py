import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    """
    Check if all numbers in fave_numbers_2 are present in fave_numbers_1
    
    Parameters
        fave_numbers_1 : list of user number 1 favorite numbers
        fave_numbers_2 : list of user number 2 favorite numbers
    
    Returns
        boolean : True if all numbers in fave_numbers_2 are present in fave_numbers_1, False otherwise
    """

    common_num = list(set(fave_numbers_2) & set(fave_numbers_1))

    return len(common_num) == len(fave_numbers_2)
