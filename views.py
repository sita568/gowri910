from django.http import HttpResponse
def greeting(request):
    return HttpResponse("hello world")
