# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Table


# create a ModelForm
class NameForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Table
        fields = "__all__"