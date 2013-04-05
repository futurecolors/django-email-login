from django.conf.urls.defaults import *

from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

# Insert email_login overrides
from email_login import adminsite
site = adminsite.EmailLoginAdminSite()

# duplicate the normal admin's registry until ticket #8500 get's fixed
site._registry = admin.site._registry


urlpatterns = patterns('',
    (r'^admin/', include(site.urls)),
    (r'^accounts/', include('email_login.urls')),
    (r'^accounts/profile/', TemplateView.as_view(template_name='email_login/base.html')),
)
