from app.libs.get_data import get_data
from flask import current_app


class search_book:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def get_isbn_book(cls, isbn_num):
        url = cls.isbn_url.format(isbn_num)
        result = get_data.get(url)
        return result

    @classmethod
    def get_key_book(cls, keyword, page=1):
        url = cls.key_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = get_data.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return current_app.config['PER_PAGE'] * (page-1)