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
    session = DBSession()
    url = request.params.get('url', '')

    # Check that the url is good (this is dirty hax, should use a regex)
    parsed = urlparse.urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        return Response('Invalid URL', status_int=503)
    elif parsed.netloc in ('www.kan.gd', 'kan.gd', 'kanged.net', 'www.kanged.net'):
        return Response('Invalid URL - This one would cause some issues ;)', status_int=503)

    try:
        obj = ShortURL(url)
        session.add(obj)
        session.commit()
    except:
        session.rollback()
        return Response('Oops!  We had an error!', status=503)

    # Encode the primary key.
    key = base36encode(obj.id)

    # Ensure the session is completely closed.
    session.commit()
    session.close()

    return Response('http://kan.gd/%s' % key)
