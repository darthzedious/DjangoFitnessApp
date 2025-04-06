from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from DjangoFitnessApp.accounts.forms import LoginForm, RegisterForm, ProfileEditForm
from DjangoFitnessApp.accounts.models import Profile

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = LoginForm

    def get_success_url(self):
        return reverse(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk
            },
        )

class UserRegisterView(CreateView):
    model = UserModel
    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(
            self.request,
            self.object,
            backend='DjangoFitnessApp.accounts.authentication.EmailOrUsernameBackend'
        )

        return response

def logout_view(request):
    logout(request)
    return redirect("login")


class LoadProfileView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'registration/profile.html'


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'registration/profile_edit.html'
    form_class = ProfileEditForm

    def test_func(self):
        """
        Ensures that the user can edit only their own profile.
        """
        profile = get_object_or_404(
            Profile,
            pk=self.kwargs['pk'],
        )

        return self.request.user == profile.user

    def form_valid(self, form):
        form.instance.profile_picture = self.request.FILES.get('profile_picture', form.instance.profile_picture)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )
