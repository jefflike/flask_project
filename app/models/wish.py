'''
__title__ = 'wish.py'
__author__ = 'Jeffd'
__time__ = '4/9/18 11:14 AM'
'''
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)