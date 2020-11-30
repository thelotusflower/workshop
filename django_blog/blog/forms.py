from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    # добавить валидаторы пароля
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
