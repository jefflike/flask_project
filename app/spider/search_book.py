# from app.libs.get_data import get_data
# from flask import current_app
#
#
# class search_book:
#     isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
#     key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
#
#     @classmethod
#     def get_isbn_book(cls, isbn_num):
#         url = cls.isbn_url.format(isbn_num)
#         result = get_data.get(url)
#         return result
#
#     @classmethod
#     def get_key_book(cls, keyword, page=1):
#         url = cls.key_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
#         result = get_data.get(url)
#         return result
#
#     @staticmethod
#     def calculate_start(page):
#         return current_app.config['PER_PAGE'] * (page-1)
from app.libs.get_data import get_data
from flask import current_app


class search_book:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def get_isbn_book(self, isbn_num):
        url = self.isbn_url.format(isbn_num)
        result = get_data.get(url)
        # print(self)
        self.__single_book_data(result)

    def get_key_book(self, keyword, page=1):
        url = self.key_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = get_data.get(url)
        self.__collection_data(result)

    def __single_book_data(self, data):
        print(self)
        self.total=1
        self.books.append(data)

    def __collection_data(self, data):
        self.total = data['total']
        self.books = data['books']

    def calculate_start(self,page):
        return current_app.config['PER_PAGE'] * (page-1)

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
