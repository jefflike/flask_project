from flask import flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.base import db
from app.models.gift import Gift
from . import web
__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    my_gift = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in my_gift]
    pass


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            # 此时已经支持事务，commit之前都没有真正提交
            gift = Gift()
            gift.isbn = isbn
            # current_user是实例化后的user模型
            gift.uid = current_user.id
            current_user.beans += 0.5
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



