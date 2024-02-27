from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView

from .views import *
from .htmx import check_username_exists

urlpatterns = [
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('registration/', Registration.as_view(), name="registration"),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='registration/password_reset.html',
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='registration/password_reset_mail_sent.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmation.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_completed.html'),
         name='password_reset_complete'),
    path('login-view/', login_view, name="login-view"),
    path('log-out/', LogoutView.as_view(next_page="home"), name="exit"),
]

htmx_urlpatterns = [
    path("registration/check-username/", check_username_exists, name="check-username")
]

urlpatterns += htmx_urlpatterns
