from django.http import HttpResponse
from myproject.settings import USERNAME

def hello_world(request):
    return HttpResponse(f"Hello World {USERNAME}")
