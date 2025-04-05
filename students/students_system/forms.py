# students_system/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Assignments, Wellness # Check spelling!


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password != password_confirmation:

            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ['title', 'due_date', 'description', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class WellnessForm(forms.ModelForm):
    class Meta:
        model = Wellness
        fields = ['mood', 'notes']
