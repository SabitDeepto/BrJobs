# from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# from .models import SolutionPost


def partners(request):
    return render(request, 'partners.html')