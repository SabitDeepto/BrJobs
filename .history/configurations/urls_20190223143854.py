from django.contrib import admin
from django.urls import include, path
# from Service import views
from TestApp.views import classroom, teachers, students


urlpatterns = [
    # path('', views.index),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Test.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    #vitor



]
