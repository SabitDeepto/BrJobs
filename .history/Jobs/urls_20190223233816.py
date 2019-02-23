# image upload setting
from configurations import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from django.conf.urls import url
from Jobs.views import home, jobpost, post, detail

urlpatterns = [
    path('', home, name='home'),
    path('jobpost', jobpost, name='jobpost'),
    path('detail', detail, name='detail'),
    path('post', post, name='post'),

    # path('service/<slug:slug>/', views.single_post_service, name='single_post_service'),
    # path('solution/<slug:slug>/', views.single_post_solution, name='single_post_solution'),
    # path('services', views.services, name='services'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()