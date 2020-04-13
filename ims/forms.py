from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    class Meta:
        model: User
        fields = ["email", "username"]
        
class ChangePasswordForm(PasswordChangeForm):
    # old_pass = forms.PasswordInput(required=True)
    # new_pass = forms.PasswordInput(required=True)
    class Meta:
        model: User
