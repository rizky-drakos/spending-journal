from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from models import ItemTypeModel, ItemTypeSchema
from extentions import db


item_type_schema = ItemTypeSchema()
item_types_schema = ItemTypeSchema(many=True)


class ItemType(Resource):

    @jwt_required
    def get(self, id):
        item_type = ItemTypeModel.query.get(id)
        return item_type_schema.dump(item_type)

    @jwt_required
    def put(self, id):
        item_type = ItemTypeModel.query.get(id)
        for k, v in request.json.items():
            if v:
                setattr(item_type, k, v)
        db.session.add(item_type)
        db.session.commit()
        return {}, 204

    @jwt_required
    def delete(self, id):
        item_type_to_delete = ItemTypeModel.query.get(id)
        db.session.delete(item_type_to_delete)
        db.session.commit()
        return {}, 204


class ItemTypes(Resource):

    @jwt_required
    def get(self):
        item_types = ItemTypeModel.query.all()
        return item_types_schema.dump(item_types)

    @jwt_required
    def post(self):
        item_type_to_add = ItemTypeModel(name=request.json["name"])
        db.session.add(item_type_to_add)
        db.session.commit()
        return item_type_schema.dump(item_type_to_add), 201
