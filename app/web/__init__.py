from flask import Blueprint


# 蓝图,__name__代表蓝图所在的模块
web = Blueprint('web', __name__, template_folder='templates')
# print(__name__) # app.web

from app.web import book_app
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish