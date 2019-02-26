from django.contrib import admin
from django.urls import include, path
from django.conf import settings
# from Service import views

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#         path('admin/', admin.site.urls),
#         path('accounts/', include('django.contrib.auth.urls')),
#         path('', include('register.urls')),
#         path('', include('Jobs.urls')),
#         path('ckeditor', include('ckeditor_uploader.urls')),


#     ] + urlpatterns


# urlpatterns = [
#     # path('', views.index),
#     path('admin/', admin.site.urls),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('', include('register.urls')),
#     path('', include('Jobs.urls')),
#     path('ckeditor', include('ckeditor_uploader.urls')),
#     #vitor


# ]
