import sys
from datetime import datetime
from flask import (
    render_template,
    flash, redirect,
    url_for,
    request,
    g,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import login, db
from app.main import main
from app.main.forms import (
    PostForm,
    SearchForm,
)
from app.models import (
    User,
    Post,
    Tag,
    Category,
)
from flask import jsonify


@main.before_app_request
def before_request():
    if current_user.is_authenticated:
        g.search_form = SearchForm()


@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    categories = Category.query.all()
    tags = Tag.query.all()
    form.category_id.choices = [(c.id, c.name) for c in categories]
    if form.validate_on_submit():
        tag_list = form.tags.data.split()
        _tags = [None] * len(tag_list)
        for i, t in enumerate(tag_list):
            _tags[i] = Tag.query.filter_by(name=t).first()
            if _tags[i] is None:
                _tags[i] = Tag(name=t)

        post = Post(title=form.title.data,
                    body=form.body.data,
                    author=current_user,
                    category_id=form.category_id.data,
                    tags=_tags)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.explore'))

    return render_template('main/index.html',
                           title='Home',
                           tags=tags,
                           categories=categories,
                           form=form)


@main.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    tags = Tag.query.all()
    categories = Category.query.all()
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('main/explore.html',
                           title='Explore',
                           tags=tags,
                           categories=categories,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url)


@main.route('/search')
@login_required
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.explore'))
    tags = Tag.query.all()
    categories = Category.query.all()
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('main/search.html',
                           title='Search',
                           posts=posts,
                           tags=tags,
                           categories=categories,
                           next_url=next_url,
                           prev_url=prev_url)
