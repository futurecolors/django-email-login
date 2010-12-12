"""
``django.contrib.admin`` unfortunatly display's an error-message telling that
you can't login with an email address. As we don't want this, we have to 
replace the whole login method...
"""
from django.contrib import admin
from forms import EmailAuthenticationForm

class EmailLoginAdminSite(admin.AdminSite):
    login_form = EmailAuthenticationForm
    login_template = 'email_login/login.html'