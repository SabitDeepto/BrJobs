from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
User = get_user_model()
# from .models import ServicePost
# from Solution.models import SolutionPost


def home(request):
    return render(request, 'basic/index.html')


def jobpost(request):
    return render(request, 'basic/client-job.html')


def post_a_job(request):
    form = JobPostForm(request.POST)
    if form.is_valid():
        ambassador = form.save()
        return redirect('ambassador_list')

    return render(request, 'forms_regular.html', {'form': form})
