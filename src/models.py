from extentions import db, ma


class ItemTypeModel(db.Model):
    __tablename__ = "item_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


class ItemTypeSchema(ma.Schema):
    class Meta:
        model = ItemTypeModel


class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    record_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    item_type_id = db.Column(db.Integer, db.ForeignKey("item_types.id"))
    item_type = db.relationship("ItemTypeModel", backref="item_type")


class ItemSchema(ma.Schema):
    class Meta:
        model = ItemModel
