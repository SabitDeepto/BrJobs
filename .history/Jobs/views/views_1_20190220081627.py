# from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# from .models import SolutionPost


def home(request):
    return render(request, 'partners.html')