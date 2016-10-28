from django import forms

class CreateUserForm(forms.Form):
    email_address = forms.EmailField(label='Email Address', max_length=50)
    password = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.PasswordInput
    )
    password_repeat = forms.CharField(
        label='Confirm Password',
        max_length=100,
        widget=forms.PasswordInput
    )
