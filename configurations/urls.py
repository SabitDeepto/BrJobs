from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
# from Service import views
urlpatterns = []

if settings.DEBUG:
    import debug_toolbar
    urlpatterns  =[
        path('__debug__/', include(debug_toolbar.urls)),
        path('admin/', admin.site.urls),
        path('accounts/', include('django.contrib.auth.urls')),
        path('', include('app_dir.Jobs.urls')),
        path('ckeditor', include('ckeditor_uploader.urls')),


    ]
    urlpatterns += i18n_patterns(
    path('', include('app_dir.Jobs.urls')),
    prefix_default_language= False,
    
)
