from django.contrib import admin
from django.urls import include, path
# from Service import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Jobs.urls')),
    path('bugbounty/', include('BugBounty.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),


]
