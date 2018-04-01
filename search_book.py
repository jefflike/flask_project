from get_data import get_data

class search_book:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def get_isbn_book(cls, isbn_num):
        url = cls.isbn_url.format(isbn_num)
        result = get_data.get(url)
        return result

    @classmethod
    def get_key_book(cls, keyword, count = 15, start = 0):
        url = cls.key_url.format(keyword, count, start)
        result = get_data.get(url)
        return result