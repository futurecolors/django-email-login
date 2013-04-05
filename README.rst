==================
django-email-login
==================

Goals
=====

The goal of this app is to easily transform django's auth system to allow
login with an email adress, instead of a username. This should work inside the
admin as well as outside. Therefore, email adresses need to be unique.

The username of the User will be the hash of it's email adress. As it means
nothing, it will be hidden in the admin changelist view.

Install
=======

Install with ``pip install django-email-login`` or checkout from Bitbucket ``hg clone https://bitbucket.org/tino/django-email-login`` and run ``python setup.py install``.

Usage
=====

1. Append ``'email_login'`` to your ``INSTALLED_APPS`` setting
#. Insert ``'email_login.auth_backend.EmailBackend'`` as first in the 
   ``AUTHENTICATION_BACKENDS`` settings tuple.
#. Add the following in you root ``urls.py`` *after* ``admin.autodiscover()``::

        # Insert email_login overrides
        from email_login import useradmin, adminsite
        site = adminsite.EmailLoginAdminSite()
        # duplicate the normal admin's registry until ticket #8500 get's fixed
        site._registry = admin.site._registry
    
#. Instead of using::

        # Uncomment the next line to enable the admin:
        (r'^admin/', include(admin.site.urls)),

   use::

        # Uncomment the next line to enable the admin:
        (r'^admin/', include(site.urls)),

   to include the admin in your root ``urls.py``.
   
#. To use login outside of the admin, add::
   
        (r'^account/', include('email_login.urls')),
   
   to your ``urls.py``

.. note:: 
    Your admin account needs to have an email address, otherwise you won't be
    able to sign in!
    
.. note::
    The admin will display the username in the top right corner of the logged
    in user if the user has no firstname. If you want to override that, over-
    ride the ``admin/base.html`` template.
    
In conjunction with django-user-creation
========================================

If you want to use this app in conjunction with `django-user-creation`_, you
have to create your own ``ModelAdmin`` for ``User``. You may do so by adding a
``useradmin.py`` file to your project with the following contents::

        from django.contrib import admin
        from django.contrib.auth.models import User
        from user_creation.forms import EmailAccountCreationForm
        from email_login.useradmin import EmailLoginAdmin


        class MyUserAdmin(EmailLoginAdmin):
            add_form = EmailAccountCreationForm
            add_fieldsets = (
                (None, {
                    'classes': ('wide',),
                    'fields': ('email', 'password1', 'password2', 'email_user')}
                ),
            )

        admin.site.unregister(User)
        admin.site.register(User, MyUserAdmin)

and adding the line ``import useradmin`` to your ``urls.py`` **after** the
overrides described above.

.. _django-user-creation: http://bitbucket.org/tino/django-user-creation
