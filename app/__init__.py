from flask import Flask
from flask_login import LoginManager

from app.models.base import db


login_manager = LoginManager()

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登陆或注册'
    # db.create_all(app=app)
    # 蓝图最后还是要注册到app核心对象中
    register_blueprint(app)

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    return app

