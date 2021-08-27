# import form class from django
from django import forms
# import GeeksModel from models.py
from .models import Deposit


# create a ModelForm
class DepositForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Deposit
        fields = "__all__"
