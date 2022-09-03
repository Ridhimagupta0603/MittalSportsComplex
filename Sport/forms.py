from django import forms

from django.contrib.auth.models import User
from .models import *

class AddSportForms(forms.ModelForm):

    class Meta():
        model = Sport
        fields = ('__all__')

class AddCourtForms(forms.ModelForm):

    class Meta():
        model = Court
        fields = ('__all__')
class AddTimeslotForms(forms.ModelForm):

    class Meta():
        model = Timeslot
        fields = ('__all__')
