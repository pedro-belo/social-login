from django.http import HttpResponseRedirect
from django.urls import reverse


def check_password(strategy, user=None, *args, **kwargs):
    if not user.has_usable_password() and user is not None:
        return HttpResponseRedirect(reverse('account:create-password'))