from django.contrib import admin
from django.urls import include, path
# from Service import views


urlpatterns = [
    # path('', views.index),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Test.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    #vitor
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),


]
