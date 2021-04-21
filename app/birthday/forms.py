from django import forms
from .models import BirthdayData


class BirthdayDataForm(forms.ModelForm):
    class Meta:
        model = BirthdayData
        fields = ('name', 'date')
