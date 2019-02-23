# image upload setting
from configurations import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('service/<slug:slug>/', views.single_post_service, name='single_post_service'),
    # path('solution/<slug:slug>/', views.single_post_solution, name='single_post_solution'),
    # path('services', views.services, name='services'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()