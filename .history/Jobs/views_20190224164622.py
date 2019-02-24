from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserForm, ProfileForm
from django.contrib import messages


from .forms import JobPostForm
from .models import JobPost


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


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            # return redirect('settings:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'basic/test.html', {
        'user_form': user_form,
        'profile_form': profile_form
})