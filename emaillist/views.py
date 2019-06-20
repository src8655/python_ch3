from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'emaillist/index.html')


def form(request):
    return render(request, 'emaillist/form.html')
