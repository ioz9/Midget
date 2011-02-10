from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from midget.models import root_factory_maker

def main(global_config, **settings):
    # Initilize SQLA engine.
    engine = engine_from_config(settings, 'sqlalchemy.')

    # Load up the root factory
    root_factory = root_factory_maker(engine)

    # Generate configuration
    config = Configurator(settings=settings, root_factory=root_factory)

    # Add the default view and dynamic view.
    config.add_view('midget.views.index', context='midget.models.Root')
    config.add_view('midget.views.redirect', context='midget.models.ShortURL')

    # Return application
    return config.make_wsgi_app()


