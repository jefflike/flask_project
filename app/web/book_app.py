from flask import jsonify

from book import app
from search_book import search_book
from search_key import key_or_isbn


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    查找书籍的信息或者isbn
    http://127.0.0.1:5000/book/search/9787501524044/1
    :param q:
    :param page:
    :return:
    """
    is_key_or_isbn = key_or_isbn(q)
    if is_key_or_isbn == 'isbn_number':
        data = search_book.get_isbn_book(q)
    else:
        data = search_book.get_key_book(q)
    # return json.dumps(data), 200 , {'content-type' : 'application/json'}
    return jsonify(data)