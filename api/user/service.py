
class UserService:
    def __init__(self):
        return

    @staticmethod
    def findWithID(id):
        from api.user import models
        user = models.User.query.filter_by(id=id).first()
        if user:
            return user
        #return models.Product.query.filter_by(title=item).all(), 200

    @staticmethod
    def UpdateUser(id,username,email):
        from api.user import models
        from api.app import db
        user = models.User.query.filter_by(id=id).first()
        user.username = username
        user.email = email
        db.session.commit()
        return user

    @staticmethod
    def AddUser(username, email):
        from api.user import models
        from api.app import db
        user = models.User(username = username, email = email,password = '123456')
        db.session.add(user)
        db.session.commit()
        return user
