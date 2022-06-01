from django import forms
from .models import *

class Current_YearForm (forms.ModelForm):
    class Meta:
        model=Current_Year
        fields='__all__'
