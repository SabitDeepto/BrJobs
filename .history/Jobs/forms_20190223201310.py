from django import forms

from .models import JobPost


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['ambassador_name', 'email', 'phone']
        widgets = {
            'ambassador_name': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Enter Ambassador name", 'type': "text"}),
            'email': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Your Email", 'type': "text"}),
            'phone': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Your phone number", 'type': "text"}),
        }
