from django import forms

from .models import JobPost


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'jobtype', 'category',
         'post_type', 'apply_url', 'validity',
         'company_name', 'company_description', 'company_website',
         'company_logo', 'company_description', 'company_website',
         ]
