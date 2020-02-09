from flask import Flask
from flask_cors import CORS

from extentions import api, db, ma
from resources.item import Item, Items
from resources.item_type import ItemType, ItemTypes

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql+pymysql://root:rootroot@mysql-container/mydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True

api.add_resource(ItemType, "/item-types/<int:id>", endpoint="item-type")
api.add_resource(ItemTypes, "/item-types", endpoint="item-types")
api.add_resource(Item, "/items/<int:id>", endpoint="item")
api.add_resource(Items, "/items", endpoint="items")

api.init_app(app)
db.init_app(app)
ma.init_app(app)
