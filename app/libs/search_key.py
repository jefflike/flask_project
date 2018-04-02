'''
判断搜索的值是关键字还是isbn号码
'''


def key_or_isbn(word):
    """
    1.放到视图函数导致view过于臃肿
    2.不利于代码重复使用
    3.不便于代码的阅读
    所以单独拿出来，重构代码
    :param word:
    :return:
    """
    search_type = 'book_name'
    short_word = word.replace('-', '')
    if len(word) == 13 and word.isdigit():
        search_type = 'isbn_number'
    # 短路操作，所以尽量将优先区别判断的放在前面，同时数据库查询放到后面
    elif '-' in word and len(short_word) == 10 and short_word.isdigit() == 10:
        search_type = 'isbn_number'
    return search_type