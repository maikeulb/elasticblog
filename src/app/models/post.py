from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.mixins import SearchableMixin


class Post(SearchableMixin, db.Model):
    __tablename__ = 'posts'
    __searchable__ = ['body']
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


db.event.listen(db.session, 'before_commit', Post.before_commit)
db.event.listen(db.session, 'after_commit', Post.after_commit)
