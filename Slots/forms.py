from django import forms
from Sport.models import *
from django.contrib.auth.models import User
from .models import *

class Bookslotform(forms.ModelForm):
    

    class Meta():
        model = slot
        fields = '__all__'
        
        

