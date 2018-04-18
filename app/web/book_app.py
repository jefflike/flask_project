from flask import jsonify, request, render_template, flash
import json

from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.search_book import search_book
from app.libs.search_key import key_or_isbn
from app.forms.search_forms import search_form
from app.view_models.book import BookCollection, BookViewModel
from app.view_models.trade import TradeInfo

from . import web


@web.route('/book/search')
def search():
    """
    查找书籍的信息或者isbn
    http://127.0.0.1:5000/book/search/9787501524044/1
    http://127.0.0.1:5000/book/search?q=9787501524044&page=1
    :param q:
    :param page:
    :return:
    """
    form = search_form(request.args)
    book = search_book()
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        is_key_or_isbn = key_or_isbn(q)

        if is_key_or_isbn == 'isbn_number':
            book.get_isbn_book(q)
        else:
            book.get_key_book(q, page)
            # data = search_book.get_key_book(q, page)

        books.fill(book, q)
        # print([b.intro for b in  books.books])
        # return json.dumps(data), 200 , {'content-type' : 'application/json'}
        # return jsonify(books.__dict__)
        # return json.dumps(books, default=lambda obj:obj.__dict__)
    else:
        flash('...')
    return render_template('search_result.html', books=books)
    #     return jsonify(form.errors)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    """
        1. 当书籍既不在心愿清单也不在礼物清单时，显示礼物清单
        2. 当书籍在心愿清单时，显示礼物清单
        3. 当书籍在礼物清单时，显示心愿清单
        4. 一本书要防止即在礼物清单，又在赠送清单，这种情况是不符合逻辑的

        这个视图函数不可以直接用cache缓存，因为不同的用户看到的视图不一样
        优化是一个逐步迭代的过程，建议在优化的初期，只缓存那些和用户无关的“公共数据"
    """
    has_in_gifts = False
    has_in_wishes = False
    # isbn_or_key = is_isbn_or_key(isbn)
    # if isbn_or_key == 'isbn':
    # 获取图书信息
    yushu_book = search_book()
    yushu_book.get_isbn_book(isbn)

    if current_user.is_authenticated:
        # 如果未登录，current_user将是一个匿名用户对象
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    book = BookViewModel(yushu_book.first)
    # if has_in_gifts:
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)
    return render_template('book_detail.html', book=book, has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model)