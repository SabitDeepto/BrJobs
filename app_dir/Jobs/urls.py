# image upload setting
from configurations import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

from django.urls import path
from ..Jobs.views import home, jobpost, single_post, update_profile, searchposts
from . import signup
prefix_default_language= False,

urlpatterns = [
    path('', home, name='home'),
    path('jobpost', jobpost, name='jobpost'),
    path('single_post/<post_id>/', single_post, name='single_post'),
    path('update_profile', update_profile, name='update_profile'),
    path('search', searchposts, name='searchposts'),
    path('signup/', signup.SignUp.as_view(), name='signup'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()