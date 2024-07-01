from flask import current_app
from random import sample
from .model import Users, Friends, db
import random

def inject_dummy_friend_requests():
  """
  Injects a random set of dummy friend requests into the Friends table and avoiding duplicates.
  """

  with current_app.app_context():
    dummy_friend_request = []
    user_ids = random.sample([user.id for user in db.session.query(Users).all()], 50)
    for user_id in user_ids:
      if user_id not in [request.from_user_id for request in db.session.query(Friends).all()]:
        dummy_friend_request.append(Friends(from_user_id=user_id))

    db.session.bulk_save_objects(dummy_friend_request)
    db.session.commit()
    print('Dummy friend request added successfully.')






  #   # Get all user IDs
  #   user_ids = [user.id for user in db.session.query(Users)]

  #   # Ensure user_count matches the actual number of users in the database
  #   if user_count != len(user_ids):
  #     print(f"Warning: Provided user_count ({user_count}) doesn't match actual user count ({len(user_ids)}). Using actual user count.")
  #     user_count = len(user_ids)

  #   # Handle edge cases
  #   if user_count <= 1:
  #     print("Warning: Not enough users to generate friend requests. Skipping.")
  #     return

  #   # Generate random requests per user with a maximum of requests_per_user
  #   requests_to_generate = [min(sample(user_ids, requests_per_user), key=lambda x: x) for _ in range(user_count)]

  #   # Flatten the list of requests (list of lists to single list)
  #   friend_requests = [item for sublist in requests_to_generate for item in sublist]

  #   # Filter out duplicates (set automatically removes duplicates)
  #   friend_requests = list(set(friend_requests))

  #   # Create Friend objects and add them to the database session
  #   new_requests = []
  #   for request in friend_requests:
  #     from_user_id, to_user_id = sample(user_ids, 2)
  #     # Ensure from_user and to_user are different users (avoid self-requests)
  #     if from_user_id != to_user_id:
  #       new_requests.append(Friends(from_user_id=from_user_id, to_user_id=to_user_id))

  #   db.session.add_all(new_requests)
  #   db.session.commit()

  #   print(f"Successfully injected {len(new_requests)} random friend requests.")

  # # Example usage (assuming you have a database connection established)
  # # user_count = get_user_count_from_database()  # Replace with your logic to get user count
  # # inject_dummy_friend_requests(db, user_count, 3)  # Generate 3 friend requests per user on average
