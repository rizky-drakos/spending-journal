from flask_restful import Resource

from models import ItemModel, ItemSchema


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


class Item(Resource):

    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class Items(Resource):

    def get(self):
        items = ItemModel.query.all()
        return items_schema.dump(items)

    def post(self):
        pass
