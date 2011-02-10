def view_root(context, request):
    return {'items':list(context), 'project':'Midget'}

def view_model(context, request):
    return {'item':context, 'project':'Midget'}
