from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from users.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['placeholder'] = fields.label


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'displayname', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['placeholder'] = fields.label


class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'displayname', 'email', 'profile')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['placeholder'] = fields.label


class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
