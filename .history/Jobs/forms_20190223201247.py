from django import forms

from .models import PostJob


class AmbassadorForm(forms.ModelForm):
    class Meta:
        model = CreateAmbassador
        fields = ['ambassador_name', 'email', 'phone']
        widgets = {
            'ambassador_name': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Enter Ambassador name", 'type': "text"}),
            'email': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Your Email", 'type': "text"}),
            'phone': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Your phone number", 'type': "text"}),
        }
