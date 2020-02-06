from flask import Flask
from flask_restful import Api

from resources.item import Item, Items
from resources.item_type import ItemType, ItemTypes


app = Flask(__name__)
api = Api()

api.add_resource(ItemType, "/item-types/<int:id>", endpoint="item-type")
api.add_resource(ItemTypes, "/item-types", endpoint="item-types")
api.add_resource(Item, "/items/<int:id>", endpoint="item")
api.add_resource(Items, "/items", endpoint="items")

api.init_app(app)
