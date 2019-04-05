from django.shortcuts import render

# Create your views here.

from django_otp.decorators import otp_required
from django.dispatch import receiver
from two_factor.compat import get_current_site
from two_factor.signals import user_verified


@otp_required
def my_view(request):
    pass

class ExampleSecretView(OTPRequiredMixin, TemplateView):
    template_name = 'secret.html'

def my_view(request):
    if request.user.is_verified():
        # user logged in using two-factor
        pass
    else:
        # user not logged in using two-factor
        pass


@receiver(user_verified)
def test_receiver(request, user, device, **kwargs):
    current_site = get_current_site(request)
    if device.name == 'backup':
        message = 'Hi %(username)s,\n\n'\
                  'You\'ve verified yourself using a backup device '\
                  'on %(site_name)s. If this wasn\'t you, your '\
                  'account might have been compromised. You need to '\
                  'change your password at once, check your backup '\
                  'phone numbers and generate new backup tokens.'\
                  % {'username': user.get_username(),
                     'site_name': current_site.name}
        user.email_user(subject='Backup token used', message=message)
