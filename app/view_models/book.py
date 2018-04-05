class BookViewModel:
    '''
    处理单本数据
    '''
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher'],
        self.author = '、'.join(book['author'])
        self.image = book['images']['large']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']
        self.isbn = book['isbn']
        # self.intros = list(filter(lambda x:True if x else False,
        #                 [self.author, self.publisher, self.price]))

    @property
    def intro(self):
        intros = filter(lambda x:True if x else False,
                        [str(self.author), str(self.publisher), str(self.price)])
        return '/'.join(intros)

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, search_book, keyword):
        self.total = search_book.total
        self.books = [BookViewModel(book) for book in search_book.books]
        self.keyword = keyword
