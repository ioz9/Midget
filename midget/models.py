# This file is part of Midget.
#
# Midget is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Midget is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Midget.  If not, see <http://www.gnu.org/licenses>
#
# Copyright (c) 2011, Chris Soyars <ctso@ctso.me>

from midget.cache import cache
from midget.lib import base36decode
from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

class ShortURL(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(Unicode(1000))

    def __init__(self, url):
        self.url = url

    @classmethod
    def get(cls, id):
        urlcache = cache.get_cache('urlcache', expire=5 * 60)

        try:
            id = base36decode(id)
        except:
                raise NoResultFound

        def get_from_database():
            session = DBSession()
            query = session.query(cls).get(id)
            return query

        return urlcache.get(id, createfunc=get_from_database)

class Root(object):
    __name__ = None
    __parent__ = None

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        # Do not bother querying the database for 'api'.
        if key == "api":
            raise KeyError
        if key == "favicon.ico":
            raise KeyError

        try:
            item = ShortURL.get(key)
            item.__parent__ = self
            item.__name__ = key
            return item
        except Exception, e:
            raise KeyError

    def get(self, key, default=None):
        try:
            item = self.__getitem__(key)
        except KeyError:
            item = default
        return item

    def __iter__(self):
        session = DBSession()
        query = session.query(ShortURL)
        return iter(query)

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

def root_factory_maker(engine):
    initialize_sql(engine)
    return Root
