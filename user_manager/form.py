
from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="(User/Company) name", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserRegisterForm(forms.Form):
	number_phone=forms.CharField(label="")
	country_code=forms.CharField(label="",widget=forms.HiddenInput())

class CompanyRegisterForm(forms.Form):
	company_username=forms.CharField(label="Company name")
	company_password=forms.CharField(label="Password",widget=forms.PasswordInput)
	company_number_phone=forms.CharField(label="whatsApp Company number")