from django import forms
from .models import Course , Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('client', 'Client'),
        ('admin', 'Admin'),
    ]
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="User Type")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'user_type')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        
        # Add additional password validation here if needed
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password1):
            raise ValidationError("Password must contain at least one letter.")
        
        return password2

    
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']
