from sqlalchemy.orm import relationship

from app.models.base import db, Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc

from app.spider.search_book import search_book


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @property
    def isbn_book(self):
        book = search_book().get_isbn_book(self.isbn).first()
        return book

    @classmethod
    def get_user_gifts(cls, uid):
        return Gift.query.filter_by(
            uid=uid,
            launched=False
        ).order_by(desc(cls.create_time)).all()

    @classmethod
    def recent(cls):
        '''
        最近上传的图书：1.只取30本，2.按时间排序，3.去重
        :return: 最近上传的30本书
        有具体业务意义的代码尽量不要写到视图函数中，写到模型层中
        '''
        recent_book = cls.query.filter_by(launched=False).group_by(
            cls.isbn).distinct().order_by(
            desc(cls.create_time)).limit(30).all()

        return recent_book