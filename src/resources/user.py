from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import UserModel, UserSchema


user_schema = UserSchema()

class User(Resource):

    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = UserModel.query.get(user_id)
        return user_schema.dump(user)
