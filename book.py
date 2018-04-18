from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from flask import current_app

from app.models.base import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
# from app.web import book_app
# add_url_rule(url, view_func， endpoint)url是路由匹配，viewfunc是视图函数

if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
