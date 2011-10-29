import base64
import hashlib

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

def email_to_username(email):
    return base64.urlsafe_b64encode(hashlib.sha256(email).digest())[:30]

class EmailAuthenticationForm(forms.Form):
    """
    Form for authenticating users by their email address.
    """
    email = forms.EmailField(label=_("Email address"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(_("Please enter a correct email address and password. Note that both fields are case-sensitive."))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("This account is inactive."))
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(
                _("Your Web browser doesn't appear to have cookies enabled. "
                  "Cookies are required for logging in."))

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

class EmailUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given email
    address and password.
    """
    email = forms.EmailField(label=_("Email address"))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
        help_text = _("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("email",)
        
    def clean_email(self):
        """ Validates that the email address is not already in use. """
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(_("A user with that email address already exists."))
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2
        
    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=False)
        user.username = email_to_username(user.email)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EmailUserChangeForm(forms.ModelForm):
    email = forms.EmailField(label=_("Email address"))
    class Meta:
        model = User
        exclude = ('username',)

    def __init__(self, *args, **kwargs):
        super(EmailUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')
            
    def save(self, commit=True):
        user = super(EmailUserChangeForm, self).save(commit=False)
        user.username = email_to_username(user.email)
        if commit:
            user.save()
        return user