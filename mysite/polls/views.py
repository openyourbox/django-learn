from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello h来了')
    # return render(request, 'index.html')