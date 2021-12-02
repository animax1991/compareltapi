from flask_restx import Resource, Namespace, fields, reqparse
from api.user.service import *
User = Namespace(name='Users', description="User API")

user_fields = User.inherit('Get User', {
    'id': fields.String(description='A User ID', required=True, example="1"),
    'username': fields.String(description='A Username', required=True, example="Han"),
    'email': fields.String(description='A User Email', required=True, example="dku@example.com")
})
parser = reqparse.RequestParser()
parser.add_argument('id', type=str)
parser.add_argument('username', type=str)
parser.add_argument('email', type=str)


@User.route('/<string:id>')
class Users(Resource):
    @User.doc('Get User By ID')
    @User.doc(response={200:'OK'})
    @User.doc(response={400:'BAD REQUEST'})
    def get(self,id):
        if UserService.findWithID(id):
            return UserService.findWithID(id).serialize(), 200
        else:
            return 'This user ID does not exist in Database'

@User.route('/')
class UserUpdate(Resource):
    @User.doc('Update user information')
    @User.expect(user_fields)
    def post(self):
        args = parser.parse_args()
        _userID = args['id']
        _userName = args['username']
        _userEmail = args['email']

        return UserService.UpdateUser(_userID,_userName,_userEmail).serialize(), 201