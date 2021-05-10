from django import forms
from .models import BirthdayData


class DateInput(forms.DateInput):
    input_type = 'date'


class BirthdayDataForm(forms.ModelForm):
    birthday = forms.DateTimeField(widget=DateInput)

    class Meta:
        model = BirthdayData
        fields = ('name', 'birthday', 'text')
