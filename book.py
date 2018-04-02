from app import create_app
from flask import current_app


app = create_app()
# from app.web import book_app
# add_url_rule(url, view_func， endpoint)url是路由匹配，viewfunc是视图函数

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=app.config['DEBUG'])
