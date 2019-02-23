from django.shortcuts import render

# from .models import ServicePost
# from Solution.models import SolutionPost


def home(request):
    return render(request, 'basic/index.html')