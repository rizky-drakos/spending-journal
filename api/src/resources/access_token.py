from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from google.oauth2 import id_token
from google.auth.transport import requests

from models import UserModel
from extentions import db

CLIENT_ID = "968308820462-4ln38bd3jnm6iegf85524knkfhr6cv7s.apps.googleusercontent.com"


class AccessToken(Resource):

    def post(self):
        google_id_token = request.json["id_token"]
        verified_token = None
        try:
            verified_token = id_token.verify_oauth2_token(google_id_token, requests.Request(), CLIENT_ID)
        except ValueError:
            print("FAILED")
        logged_in_user = UserModel.query.filter_by(email=verified_token["email"]).first()
        if not logged_in_user:
            new_user = UserModel(
                name = verified_token["name"],
                email = verified_token["email"],
                picture_url = verified_token["picture"]
            )
            db.session.add(new_user)
            db.session.commit()
            logged_in_user = new_user
        access_token = create_access_token(identity=logged_in_user.id, expires_delta=False)
        return {"access_token": access_token}, 201

    def get(self):
        access_token = create_access_token(identity=1, expires_delta=False)
        return {"access_token": access_token}, 201