from django.http import HttpResponse

def home(request):
    return HttpResponse("<a href = 'shop'>shop</a>")