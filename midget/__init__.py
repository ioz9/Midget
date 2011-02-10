from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from midget.models import appmaker

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    get_root = appmaker(engine)
    config = Configurator(settings=settings, root_factory=get_root)
    config.add_static_view('static', 'midget:static')
    config.add_view('midget.views.view_root', 
                    context='midget.models.MyApp', 
                    renderer="templates/root.pt")
    config.add_view('midget.views.view_model',
                    context='midget.models.MyModel',
                    renderer="templates/model.pt")
    return config.make_wsgi_app()


