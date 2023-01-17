from django import forms
from .models import Route

class RouterForm(forms.ModelForm):
    
    class Meta:
        model = Route
        fields = '__all__'