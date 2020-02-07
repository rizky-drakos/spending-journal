from flask_restful import Resource


from models import ItemTypeModel, ItemTypeSchema


item_type_schema = ItemTypeSchema()
item_types_schema = ItemTypeSchema(many=True)


class ItemType(Resource):

    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class ItemTypes(Resource):

    def get(self):
        item_types = ItemTypeModel.query.all()
        return item_types_schema.dump(item_types)

    def post(self):
        pass
