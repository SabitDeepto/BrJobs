from django import forms
from .models import JobPost, Profile, User

# from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'jobtype', 'category',
         'post_type', 'apply_url',
         'company_name', 'company_description', 'company_website',
         'company_logo', 'twitter_link',
         ]


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')
