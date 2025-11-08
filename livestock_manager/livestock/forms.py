
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Livestock

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ['animal_name', 'animal_type', 'breed', 'age', 'health_status']
