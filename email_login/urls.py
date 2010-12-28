# We need to override login view, the rest is ok.
from django.conf.urls.defaults import *
from django.contrib.auth.urls import urlpatterns as auth_urls
from forms import EmailAuthenticationForm

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', 
        { 'template_name' : 'email_login/login.html',
          'authentication_form' : EmailAuthenticationForm}),
)

urlpatterns += auth_urls