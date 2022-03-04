from django.http import HttpResponse


def hello_world(request):
    """The REST endpoint to return 'Hello World!'."""
    # Could only allow GETs (to imply incoming POSTs won't be processed)?
    return HttpResponse('Hello World!')
