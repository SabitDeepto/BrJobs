# image upload setting
from configurations import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from django.conf.urls import url
from . views import update_profile

urlpatterns = [
    path('', views_1.home, name='home'),
    path('update_profile', views_1.update_profile, name='update_profile'),


]