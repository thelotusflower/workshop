from django import forms


def validate_password(value):
    if value in {'password', '123456789', '987654321'}:
        raise forms.ValidationError(
            'Пароль слишком простой!', code='invalid',
        )


class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    # добавить валидаторы пароля
    password = forms.CharField(
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput(),
        required=True,
        validators=[validate_password]
    )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
