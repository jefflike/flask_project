from flask import jsonify, request, render_template, flash
import json


from app.spider.search_book import search_book
from app.libs.search_key import key_or_isbn
from app.forms.search_forms import search_form
from app.view_models.book import BookCollection, BookViewModel

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
    book = search_book()
    book.get_isbn_book(isbn)
    books = BookViewModel(book.books[0])
    return render_template('book_detail.html', book=books, wishes=[], gifts=[])