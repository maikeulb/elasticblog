from app.extensions import db


class Category(db.Model):
    __tablename__ = 'categories'
    __searchable__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
