from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import match, search, accept_friend, view_friend_requests, view_friends,\
     inject_dummy_data, inject_dummy_friend_request, unfriend, create_account

from .model import db

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route("/")
    def hello():
        return "Hello World!"
    
    app.register_blueprint(match.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(accept_friend.bp)
    app.register_blueprint(view_friends.bp)
    app.register_blueprint(view_friend_requests.bp)
    app.register_blueprint(unfriend.bp)
    app.register_blueprint(create_account.bp)

    @app.cli.command('add-dummy-data')
    def inject_dummy_data_command():
        inject_dummy_data.add_dummy_data()

    @app.cli.command('add-dummy-friend-request')
    def inject_dummy_friend_requests_command():
        inject_dummy_friend_request.inject_dummy_friend_requests()

    with app.app_context():
        # from .model import Users
        db.create_all()

    return app
