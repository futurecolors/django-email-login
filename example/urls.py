from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Insert email_login overrides
from email_login import useradmin, adminsite
site = adminsite.EmailLoginAdminSite()
# duplicate the normal admin's registry until ticket #8500 get's fixed
site._registry = admin.site._registry

urlpatterns = patterns('',
    # Example:
    # (r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(site.urls)),
)
