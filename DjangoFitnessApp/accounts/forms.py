from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from DjangoFitnessApp.accounts.models import Profile
from DjangoFitnessApp.mixins import PlaceholderMixin

UserModel = get_user_model()


class LoginForm(PlaceholderMixin, AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username or email'
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )


class RegisterForm(PlaceholderMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username','email']


class ProfileEditForm(forms.ModelForm):
    # profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['profile_picture', 'first_name', 'last_name', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AppUserChangeForm(PlaceholderMixin, UserChangeForm):
    """Used in the admin functionality."""
    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'
