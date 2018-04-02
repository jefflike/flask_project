from flask import Blueprint


# 蓝图,__name__代表蓝图所在的模块
web = Blueprint('web', __name__)
# print(__name__) # app.web

from app.web import book_app