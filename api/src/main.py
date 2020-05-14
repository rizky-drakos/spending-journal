import datetime

from flask import Flask
from flask_cors import CORS

from extentions import api, db, ma, jwt, migrate
from resources.item import Item, Items
from resources.item_type import ItemType, ItemTypes
from resources.user import User
from resources.cost_by_item_types import CostByItemTypes
from resources.access_token import AccessToken

app = Flask(__name__)
cors = CORS(app, resources="/*")

app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql+pymysql://root:rootroot@db/mydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_SECRET_KEY'] = \
    '672B93FD95B542EABD0E5E4A5FF41413F3894E2C7C21B57390A069B7E5EC86D2'
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(seconds=5)


api.add_resource(ItemType, "/item-types/<int:id>", endpoint="item-type")
api.add_resource(ItemTypes, "/item-types", endpoint="item-types")

api.add_resource(Item, "/items/<int:id>", endpoint="item")
api.add_resource(Items, "/items", endpoint="items")

api.add_resource(User, "/user", endpoint="user")

api.add_resource(CostByItemTypes, "/cost-by-item-types", endpoint="cost-by-item-types")

api.add_resource(AccessToken, "/access-token", endpoint="access-token")
api.add_resource(AccessToken, "/guest-token", endpoint="guest-token")

api.init_app(app)
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
migrate.init_app(app, db)
