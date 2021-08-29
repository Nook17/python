# import form class from django
from django import forms
# import GeeksModel from models.py
from .models import Deposit, Withdrawal, Notesdb


# create a ModelForm
class DepositForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Deposit
        fields = "__all__"


# create a ModelForm
class WithdrawalForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Withdrawal
        fields = "__all__"


class NotesdbForm(forms.ModelForm):
    class Meta:
        model = Notesdb
        fields = "__all__"
