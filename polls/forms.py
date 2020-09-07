from django import forms
from .models import Choice,Question

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'