from app.extensions import db


class Tag(db.Model):
    __tablename__ = 'tags'
    __searchable__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
