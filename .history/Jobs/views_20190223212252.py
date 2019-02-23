from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import JobPostForm

# from .models import ServicePost
# from Solution.models import SolutionPost


def home(request):
    return render(request, 'basic/index.html')


def jobpost(request):
    form = JobPostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'basic/client-job.html', {'form': form})


def post(request):
    form = JobPostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'basic/test.html', {'form': form})
