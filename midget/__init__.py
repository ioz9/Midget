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


from midget.models import root_factory_maker, DBSession
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

class SessionRemoverMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, *args, **kwargs):
        try:
            return self.app(*args, **kwargs)
        finally:
            DBSession.remove()

def main(global_config, **settings):
    # Initilize SQLA engine.
    engine = engine_from_config(settings, 'sqlalchemy.')

    # Load up the root factory
    root_factory = root_factory_maker(engine)

    # Generate configuration
    config = Configurator(settings=settings, root_factory=root_factory)

    # Add the default view and dynamic view.
    config.add_static_view(name='static', path='midget:static')
    config.add_view('midget.views.index', renderer='index.mako')
    config.add_view('midget.views.api', name='api')
    config.add_view('midget.views.redirect', context='midget.models.ShortURL')

    # Return application
    return SessionRemoverMiddleware(config.make_wsgi_app())


