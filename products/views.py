from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("Hello, world! This is the products app.")
