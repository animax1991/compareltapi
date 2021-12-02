from api import db
from api.common.ORMModel import ORMModel


# authorize a user for login & sign up part

class User(ORMModel):
    __tablename__ = 'user'

    # declare User Table Columns
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, username, email, password, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email
        self.password = password

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def __repr__(self):
        return f"User('{self.id}')"

    def __unicode__(self):
        return self.id or ''

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }
