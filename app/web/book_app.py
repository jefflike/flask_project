from flask import jsonify, request


from app.spider.search_book import search_book
from app.libs.search_key import key_or_isbn
from app.forms.search_forms import search_form

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
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        is_key_or_isbn = key_or_isbn(q)
        if is_key_or_isbn == 'isbn_number':
            data = search_book.get_isbn_book(q)
        else:
            data = search_book.get_key_book(q, page)
        # return json.dumps(data), 200 , {'content-type' : 'application/json'}
        return jsonify(data)
    else:
        return jsonify(form.errors)