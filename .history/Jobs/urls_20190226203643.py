# image upload setting
from configurations import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from Jobs.views import home, jobpost,  single_post, update_profile, searchposts, test, create_user

urlpatterns = [
    path('', home, name='home'),
    path('jobpost', jobpost, name='jobpost'),
    path('single_post/<post_id>/', single_post, name='single_post'),
    path('update_profile', update_profile, name='update_profile'),
    path('search', searchposts, name='searchposts'),
    path('user', test, name='test'),
    path('user', create_user, name='create_user'),


    # path('service/<slug:slug>/', views.single_post_service, name='single_post_service'),
    # path('solution/<slug:slug>/', views.single_post_solution, name='single_post_solution'),
    # path('services', views.services, name='services'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()