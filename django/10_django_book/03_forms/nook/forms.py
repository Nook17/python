from django import forms
from django.core.exceptions import ValidationError

BOOK_CHOICES = (('Programming', (('1', 'Deep Learning with Karas'), ('2', 'Web Development with Django'))),
                ('Technology', (('3', 'C++'), ('4', 'Python'))))
RADIO_CHOICES = (('first', 'first'), ('second', 'second'), ('third', 'third'))


class NookForm(forms.Form):
    text_input = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name"}), max_length=5, required=False)
    password_input = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}), min_length=8)
    checkbox_on = forms.BooleanField()
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICES)
    book_you_own = forms.MultipleChoiceField(choices=BOOK_CHOICES)
    radio_input = forms.ChoiceField(initial="first", choices=RADIO_CHOICES, widget=forms.RadioSelect)
    text_area = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Type Your story"}))
    integer_input = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Number"}), max_value=10_000)
    float_input = forms.FloatField(initial="2.4", min_value=5)
    decimal_input = forms.DecimalField(max_digits=4, decimal_places=2)
    email_input = forms.EmailInput()
    date_input = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


def validateLowercaseNook(value):
    if value.lower() != value:
        raise ValidationError("{} has UPPERCASE letters.".format(value))

def validateEmailCompany(value):
    if value.split("@")[-1].lower() != "nook17.pl":
        raise ValidationError("Your email address must by in the domain 'nook17.pl' !!!")


class NookForm3(forms.Form):
    text_input = forms.CharField(validators=[validateLowercaseNook], label="Validated text")
    signup = forms.BooleanField(label='Do you want to receive the newsletter?', required=False)
    email = forms.EmailField(validators=[validateEmailCompany],
                             help_text="Write your e-mail to receive the Newsletter", required=False,
                             widget=forms.EmailInput(attrs={"placeholder": "Company e-mail"}))
    item_a = forms.IntegerField(min_value=0, max_value=100)
    item_b = forms.IntegerField(min_value=0, max_value=100)

    def clean(self):
        cleaned_data = super().clean()  # Pobiera oczyszczone dane z formularza
        if cleaned_data["signup"] and not cleaned_data.get("email"):
            self.add_error("email", "If you want to receive the Newsletter, you must write an e-mail.")
        if cleaned_data.get("item_a", 0) + cleaned_data.get("item_b", 0) > 100:
            self.add_error(None, "the total number of elements cannot exceed 100.")