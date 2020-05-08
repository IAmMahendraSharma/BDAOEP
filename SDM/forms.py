from django import forms

class StudentForm(forms.Form):
	pen = forms.IntegerField(label = 'PEN')
	name = forms.CharField(label = 'Name', max_length = 20)
	email = forms.EmailField(label = 'Email')
	mobile = forms.IntegerField(label = 'Mobile')
	pen = forms.IntegerField(label = 'PEN')


class LoginForm(forms.Form):
	email = forms.EmailField(label = 'Email')
	password = forms.CharField(widget = forms.PasswordInput())
