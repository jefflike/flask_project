from flask import render_template

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web


__author__ = '七月'


@web.route('/')
def index():
    books = [BookViewModel(gift.isbn_book) for gift in Gift.recent()]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
