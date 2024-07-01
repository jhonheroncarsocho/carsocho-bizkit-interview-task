from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    occupation = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'

class Friends(db.Model):
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')

    def __repr__(self):
        return f'<Friend {self.id}>'
