# image upload setting
from configurations import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from django.conf.urls import url
from . views import views_1

urlpatterns = [
    path('', views_1.home, name='home'),
    path('test', views_1.test, name='test'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()
