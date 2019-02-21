# image upload setting
from configurations import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('solutions', views.solution_page, name='solution_page'),
    # path('solutions/<slug:slug>/', views.single_post_solution, name='single_post_solution'),
    # path('view_solution', views.view_solution, name='view_solution'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()
