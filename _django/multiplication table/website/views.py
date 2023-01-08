from django.http import HttpResponse
import os
from django.shortcuts import render

def index(request):
    mul = request.GET.get('text' , 0)
    if mul != 0:
        return HttpResponse(int(mul)*4)
    else:
        return render(request , 'index.html')

def tables(request):
    mul = request.GET.get('text' , 'default')
    return HttpResponse(int(mul)*2)