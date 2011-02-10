import transaction

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from sqlalchemy import Column, Integer, Unicode

from zope.sqlalchemy import ZopeTransactionExtension

from midget.lib import base36decode

#DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
DBSession = scoped_session(sessionmaker())
Base = declarative_base()

class ShortURL(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(Unicode(1000))

    def __init__(self, url):
        self.url = url

class Root(object):
    __name__ = None
    __parent__ = None

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        session= DBSession()
        try:
            id = base36decode(key)
        except:
            raise KeyError(key)

        query = session.query(ShortURL).filter_by(id=id)

        try:
            item = query.one()
            item.__parent__ = self
            item.__name__ = key
            return item
        except NoResultFound:
            raise KeyError(key)
        finally:
            DBSession.remove()

    def get(self, key, default=None):
        try:
            item = self.__getitem__(key)
        except KeyError:
            item = default
        return item

    def __iter__(self):
        session= DBSession()
        query = session.query(ShortURL)
        DBSession.remove()
        return iter(query)

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

def root_factory_maker(engine):
    initialize_sql(engine)
    return Root
