from django.http import HttpResponse

USERNAME = "Amirhosein Ghiasi"

def hello_world(request):
    return HttpResponse(f"Hello World {USERNAME}")
