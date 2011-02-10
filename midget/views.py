from pyramid.httpexceptions import HTTPFound

def index(request):
    return {}

def redirect(context, request):
    return HTTPFound(location=context.url)
