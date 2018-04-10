import config
import os
from flask import (
    Flask,
    render_template,
    current_app)
from app.extensions import (
    bcrypt,
    csrf_protect,
    db,
    login,
    migrate,
    moment)
from app.account import account as account_bp
from app.main import main as main_bp
from elasticsearch import Elasticsearch


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None
    register_blueprints(app)
    register_extensions(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(account_bp, url_prefix='/account')
    app.register_blueprint(main_bp)
    return None


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
