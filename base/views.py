from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def login(request):
    return render(request, 'log-in.html')