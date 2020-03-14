from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from models import ItemModel, ItemSchema
from extentions import db

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


class Item(Resource):

    @jwt_required
    def get(self, id):
        item = ItemModel.query.get(id)
        return item_schema.dump(item)

    @jwt_required
    def put(self, id):
        item = ItemModel.query.get(id)
        for k, v in request.json.items():
            setattr(item, k, v)
        db.session.add(item)
        db.session.commit()
        return {}, 204

    @jwt_required
    def delete(self, id):
        item_to_delete = ItemModel.query.get(id)
        db.session.delete(item_to_delete)
        db.session.commit()
        return {}, 204


class Items(Resource):

    @jwt_required
    def get(self):
        items = ItemModel.query.all()
        return items_schema.dump(items)

    @jwt_required
    def post(self):
        item_to_add = ItemModel(
            name=request.json["name"],
            record_date=request.json["record_date"],
            item_type_id=request.json["item_type_id"],
            amount=request.json["amount"]
        )
        db.session.add(item_to_add)
        db.session.commit()
        return item_schema.dump(item_to_add), 201
