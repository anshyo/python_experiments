from django.shortcuts import render , HttpResponse

# Create your views here
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<h1>hey</h1>")

def services(request):
    return HttpResponse("<h1>hey</h1>")
