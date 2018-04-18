from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy import String, Boolean
from sqlalchemy import Integer, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.search_key import key_or_isbn
from app.models.base import db, Base
from app import login_manager
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.search_book import search_book


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column('鱼豆', Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    gifts = relationship('Gift')

    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        # 这个方法帮我们完成先加密再对比的操作
        return check_password_hash(self._password, raw)

    # def get_id(self):
    # UserMixin解决了获取用户唯一标识的问题，如果唯一标识不是id那么需要定义次字段
    #     return self.id

    def can_save_to_list(self, isbn):
        if key_or_isbn(isbn) != 'isbn':
            return False
        yushu_book = search_book()
        yushu_book.get_isbn_book(isbn)
        if not yushu_book.first:
            return False
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False

#flask-login 调用
@login_manager.user_loader
def get_id(uid):
    # cookie里只存储了uid，在这里将id号转化成了用户模型
    return User.query.get(int(uid))
