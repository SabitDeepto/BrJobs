from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import JobPostForm
from .models import JobPost

# from .models import ServicePost
# from Solution.models import SolutionPost


def home(request):
    post = JobPost.objects.all()
    return render(request, 'basic/index.html', {'post': post})


def single_post(request, post_id):
	post = JobPost.objects.get(pk=post_id)
	return render(request, 'basic/detail.html', {'post': post})


def jobpost(request):
    form = JobPostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'basic/client-job.html', {'form': form})


def get_uid(request):
    return render(request, )
