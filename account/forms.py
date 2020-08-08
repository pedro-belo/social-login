from django import forms
from django.contrib.auth.forms import UserCreationForm as CreationForm, SetPasswordForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


User = get_user_model()


class UserCreationForm(CreationForm):

    email = forms.EmailField(required=True)

    def save(self, commit=True):

        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        super().save(commit)

class CreatePassword(forms.ModelForm):

    repeat_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['password']

    def clean_repeat_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('repeat_password')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError('Senha e repitir senha devem ser iguais.')
        password_validation.validate_password(password2, user=None)
        return password2

    def save(self, commit=True):
        self.instance.password = make_password(self.cleaned_data['password'])
        super().save(commit)

