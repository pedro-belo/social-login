from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views.generic.base import View
from social_django.models import UserSocialAuth

from account.forms import CreatePassword, UserCreationForm


class CreatePasswordView(LoginRequiredMixin, View):

    template_name = 'registration/create_password.html'
    Form = CreatePassword

    def is_allowed(self, request):
        if request.user.has_usable_password():
            raise PermissionDenied

    def get(self, request, *args, **kwargs):
        self.is_allowed(request)
        return render(request,
                      self.template_name,
                      context={'form': self.Form()})

    def post(self, request, *args, **kwargs):
        self.is_allowed(request)
        form = self.Form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return render(request,
                          self.template_name,
                          context={'change': True})

        return render(request, self.template_name, context={'form': form})


class UserCreationView(View):

    template_name = 'registration/create.html'
    Form = UserCreationForm

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      context={'form': self.Form()})

    def post(self, request, *args, **kwargs):

        form = self.Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')

        return render(request, self.template_name, context={'form': form})


@login_required
def settings(request):

    template_name = 'account/settings.html'

    social_accounts = UserSocialAuth.objects.filter(user=request.user)
    context = {'social_accounts': social_accounts}

    return render(request, template_name, context=context)
