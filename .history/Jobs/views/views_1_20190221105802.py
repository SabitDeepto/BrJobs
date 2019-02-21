# from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# from .models import SolutionPost


def home(request):
    return render(request, 'basic/index.html')


def test(request):
    return render(request, 'test.html')
