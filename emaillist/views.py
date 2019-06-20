from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'emaillist/index.html')


def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    firstname = request.POST['fn']
    lastname = request.POST['ln']
    email = request.POST['email']

    return render(request, 'emaillist/add.html')
