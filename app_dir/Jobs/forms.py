from django import forms
from .models import JobPost, Profile

# from .models import User
from django.contrib.auth.models import User

# from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'jobtype', 'category',
         'post_type', 'apply_url',
         'company_name', 'company_description', 'company_website',
         'company_logo', 'twitter_link',
         ]
        widgets = {
            'category': forms.Select(attrs={'class': "form-control select2", 'placeholder': "Choose Category"}),
        }



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ('bio', 'location', 'profile_picture')