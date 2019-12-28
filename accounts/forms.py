from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['placeholder'] = fields.label

class CreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'displayname', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['placeholder'] = fields.label

