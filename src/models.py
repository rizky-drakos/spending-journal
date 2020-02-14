from extentions import db, ma


class ItemTypeModel(db.Model):
    __tablename__ = "item_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    items = db.relationship(
        "ItemModel",
        backref="item_type",
        cascade="all, delete-orphan"
    )


class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    record_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    item_type_id = db.Column(
        db.Integer, db.ForeignKey("item_types.id"),
        nullable=False
    )


class ItemTypeSchema(ma.ModelSchema):
    class Meta:
        fields = ("id", "name")


class ItemSchema(ma.ModelSchema):
    class Meta:
        fields = ("id", "name", "record_date", "amount", "item_type")
    item_type = ma.Pluck(ItemTypeSchema, "name")

# it's better to place Model Classes next to each other,
# otherwise you'll get an error that it can't locate class
# name from SqlAlchemy.
