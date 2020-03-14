from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


api = Api()
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
