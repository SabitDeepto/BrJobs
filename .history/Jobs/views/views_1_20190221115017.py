# from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'basic/index.html')


def test(request):
    return render(request, 'test.html')


# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()