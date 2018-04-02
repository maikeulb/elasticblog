from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.models.mixins import SearchableMixin
from app.models.tag import Tag
from app.models.category import Category

tag_posts = db.Table(
    'tag_posts',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'))
)


class Post(SearchableMixin, db.Model):
    __tablename__ = 'posts'
    __searchable__ = ['body', 'title', 'category_name', 'tag_names',
                      'author_username']

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    title = db.Column(db.String())
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    category = db.relationship(
        'Category',
        backref='post',
        lazy='select',
    )

    tags = db.relationship(
        'Tag',
        secondary=tag_posts,
        backref='post'
    )

    @property
    def category_name(self):
        return self.category.name

    @property
    def tag_names(self):
        return [t.name for t in self.tags]

    @property
    def author_username(self):
        return self.author.username


db.event.listen(db.session, 'before_commit', Post.before_commit)
db.event.listen(db.session, 'after_commit', Post.after_commit)
