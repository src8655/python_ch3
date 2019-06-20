from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, 'helloworld/hello.html')


def hello2(request, id=0):
    return HttpResponse('id:{0}'.format(id))
