from django import forms

from .models import JobPost


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'jobtype', 'category',
         'post_type', 'apply_url', 'validity',
         'company_name', 'apply_url', 'validity',
         ]
