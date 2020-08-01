from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def login(request):
    return render(request, 'log-in.html')

@login_required
def user_area(request):
    return render(request, 'user_area.html')
