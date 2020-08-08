from django.core.exceptions import PermissionDenied
from django.views.generic.base import View
from django.shortcuts import render, redirect
from account.forms import UserCreationForm, CreatePassword
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash

class CreatePasswordView(LoginRequiredMixin, View):

    template_name = 'registration/create_password.html'
    Form = CreatePassword

    def is_allowed(self, request):
        if request.user.has_usable_password():
            raise PermissionDenied

    def get(self, request, *args, **kwargs):
        self.is_allowed(request)
        return render(request, self.template_name, context={'form': self.Form()})

    def post(self, request, *args, **kwargs):
        self.is_allowed(request)
        form = self.Form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return render(request, self.template_name, context={'change': True})

        return render(request, self.template_name, context={'form': form})

class UserCreationView(View):
    
    template_name = 'registration/create.html'
    Form = UserCreationForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.Form()})

    def post(self, request, *args, **kwargs):
    
        form = self.Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
            
        return render(request, self.template_name, context={'form': form})

@login_required
def settings(request):
    social_accounts = UserSocialAuth.objects.filter(user=request.user)
    return render(request, 'account/settings.html', context={'social_accounts': social_accounts})
