from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.views.generic import ListView

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model, login

from registration.forms import RegisterUserForm, LoginForm
from main_app.mixins import HeaderMixin
from .utils import account_activation_token


User = get_user_model()


class Registration(HeaderMixin, View):
    template_name = "registration/registration.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))

        registration_form = RegisterUserForm()
        return render(request, 'registration/registration.html', {
            'form': registration_form,
        })

    def post(self, request, *args, **kwargs):
        registration_form = RegisterUserForm(request.POST)

        if registration_form.is_valid():
            # save registration_form in the memory not in database
            user = registration_form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = registration_form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.add_message(request, messages.INFO, "Please confirm your email to activate your account")
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, 'registration/registration.html', {
                'form': registration_form,
            })


def login_view(request):
    form = AuthenticationForm(request.POST)
    if form.is_valid():
        login(request, form.get_user())
        return HttpResponseRedirect(reverse("home"))

    return HttpResponseRedirect(reverse("registration"))


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.SUCCESS, "<strong>Well done!</strong> The account is activated. Now you can log in to the site!")
    else:
        messages.add_message(request, messages.ERROR, "Link is <strong>invalid</strong> or <strong>expired</strong>")
    return HttpResponseRedirect(reverse("home"))
