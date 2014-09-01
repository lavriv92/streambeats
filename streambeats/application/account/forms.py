from django import forms
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    """
    Form for create custom user in admin.
    """
    password1 = forms.CharField(
        label=_('password'),
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('confirm password'),
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1', None)
        password2 = self.cleaned_data.get('password2', None)

        if password1 is not None and password2 is not None\
                and password1 != password2:
            raise forms.ValidationError(_('Passwords don\'t match'))

    def save(self, commit=True):
        password = self.cleaned_data.get('password1')
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(password)

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    Form for edit custom user in admin.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

    def clean_password(self):
        return self.initial['password']


class LoginForm(forms.Form):
    """
    login form
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Username or email')
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Password')
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login()
        return cleaned_data


class RegisterForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Username')
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Email')
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Password')
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )
