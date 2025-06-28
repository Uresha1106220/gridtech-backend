from . import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(50))
    subcategories = db.Column(db.String(255))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    category = db.Column(db.String(80))
    subcategory = db.Column(db.String(80))
    image_url = db.Column(db.String(255))
    status = db.Column(db.String(50))

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_email = db.Column(db.String(120))
