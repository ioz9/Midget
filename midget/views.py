from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from midget.models import ShortURL, DBSession
from midget.lib import base36encode
import urlparse

def index(request):
    return {}

def redirect(context, request):
    return HTTPFound(location=context.url)

def api(request):
    # Grab a session from sessionmaker.
    session = DBSession()

    # Grab url from querystring.
    url = request.params.get('url', '')

    # Check that the url is good (this is dirty hax, should use a regex)
    parsed = urlparse.urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        return Response('Invalid URL', status_int=503)

    try:
        session = DBSession()
        obj = ShortURL(url)
        session.add(obj)
        session.commit()
    except:
        session.rollback()
        return Response('Oops!  We had an error!', status=503)

    # Encode the primary key.
    key = base36encode(obj.id)

    # Remove the session.
    DBSession.remove()

    return Response('http://kan.gd/%s' % key)
