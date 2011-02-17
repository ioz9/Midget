from midget.models import root_factory_maker, DBSession
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

__version__ = '0.9'

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
    return config.make_wsgi_app()


