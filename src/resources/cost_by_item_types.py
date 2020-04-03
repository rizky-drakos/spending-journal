from flask_restful import Resource
from sqlalchemy import func, cast

from models import ItemModel, ItemTypeModel, CostByItemTypesSchema
from extentions import db


cost_by_item_types_schema = CostByItemTypesSchema(many=True)


class CostByItemTypes(Resource):

    def get(self):
        cost_by_item_types = \
        db.session \
        .query(ItemTypeModel.name, cast(func.sum(ItemModel.amount), db.Integer).label("cost")) \
        .join(ItemTypeModel.items).group_by(ItemTypeModel.name).all()
        return cost_by_item_types_schema.dump(cost_by_item_types)