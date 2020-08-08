from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'base/index.html')


@login_required
def user_area(request):
    return render(request, 'user_area.html')
