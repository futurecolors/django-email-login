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

.. note:: 
	Your admin account needs to have an email address, otherwise you won't be
	able to sign in!
	
.. note::
	The admin will display the username in the top right corner of the logged
	in user if the user has no firstname. If you want to override that, over-
	ride the ``admin/base.html`` template.