
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Livestock

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ['owner', 'animal_name', 'animal_type', 'breed', 'age', 'health_status']
