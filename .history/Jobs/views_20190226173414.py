from django.shortcuts import redirect, render
from .forms import UserForm, ProfileForm
from .models import JobPost, AppliedJob
from django.contrib import messages
from django.db.models import Q
from .forms import JobPostForm


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


def searchposts(request):
    if request.method == 'GET':

        title = request.GET.get('p')
        location = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if title is not None and location is not None:
            lookups = Q(title__icontains=title) & Q(location__icontains=location)

            results = JobPost.objects.filter(lookups).distinct()

            context = {'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'basic/index.html', context)

        else:
            return render(request, 'basic/index.html')

    else:
        return render(request, 'basic/index.html')


def test(request):
    user = request.user
    x = AppliedJob.object.create()
    return render(request, "test.html", {'user':user})