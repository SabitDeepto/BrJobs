from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# from .models import ServicePost
# from Solution.models import SolutionPost


def home(request):
    return render(request, 'basic/index.html')


def jobpost(request):
    return render(request, 'basic/client-job.html')
