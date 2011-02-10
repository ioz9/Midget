from pyramid.httpexceptions import HTTPFound

def index(request):
    return Response("index")

def redirect(context, request):
    return HTTPFound(location=context.url)
