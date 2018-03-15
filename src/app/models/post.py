from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.mixins import SearchableMixin

tag_posts = db.Table(
    'tag_posts',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'))
)


class Post(SearchableMixin, db.Model):
    __tablename__ = 'posts'
    __searchable__ = ['body', 'category']

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(45))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    tags = db.relationship(
        "Tag",
        backref='post',
    )


db.event.listen(db.session, 'before_commit', Post.before_commit)
db.event.listen(db.session, 'after_commit', Post.after_commit)
