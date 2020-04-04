from flask import request
from flask_restful import Resource
from sqlalchemy import func, cast, extract

from models import ItemModel, ItemTypeModel, CostByItemTypesSchema
from extentions import db


cost_by_item_types_schema = CostByItemTypesSchema(many=True)


class CostByItemTypes(Resource):

    def post(self):
        cost_by_item_types = \
        db.session.query(ItemTypeModel.name, cast(func.sum(ItemModel.amount), db.Integer).label("cost")) \
        .join(ItemTypeModel.items) \
        .filter(extract('year', ItemModel.record_date)==request.json["year"], extract('month', ItemModel.record_date)==request.json["month"]) \
        .group_by(ItemTypeModel.name).all()
        return cost_by_item_types_schema.dump(cost_by_item_types)