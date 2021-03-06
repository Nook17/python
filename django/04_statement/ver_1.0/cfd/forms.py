# import form class from django
from django import forms
# import GeeksModel from models.py
from .models import Deposit, Withdrawal, Notesdb, Buy_calc, Quarter, Pipmargin


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
        # widgets = {
        #     'buy_or_sell': forms.RadioSelect
        # }


class Buy_calcForm(forms.ModelForm):
    class Meta:
        model = Buy_calc
        fields = "__all__"


class QuarterForm(forms.ModelForm):
    class Meta:
        model = Quarter
        fields = "__all__"


class PipmarginForm(forms.ModelForm):
    class Meta:
        model = Pipmargin
        fields = "__all__"
