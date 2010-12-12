"""
Override the add- and change-form in the admin, to hide the username.
"""
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from forms import EmailUserCreationForm, EmailUserChangeForm

class EmailLoginAdmin(UserAdmin):
    add_form = EmailUserCreationForm
    form = EmailUserChangeForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    
# Override User's __unicode__ method to display something legible instead of
# a hexdigest
def __email_unicode__(self):
    if self.get_full_name():
        return self.get_full_name()
    return self.email
    
User.add_to_class('__unicode__', __email_unicode__)
    
admin.site.unregister(User)
admin.site.register(User, EmailLoginAdmin)