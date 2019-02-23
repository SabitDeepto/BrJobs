from django.shortcuts import render

# from .models import ServicePost
# from Solution.models import SolutionPost


def home(request):
    # service_post = ServicePost.objects.all()
    # solution_post = SolutionPost.objects.all()
    # context = {
    #     'service_post': service_post,
    #     'solution_post': solution_post
    #     }
    return render(request, 'basic/index.html')