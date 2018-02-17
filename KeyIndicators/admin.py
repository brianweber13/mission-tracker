from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, Investigator

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# see: https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#extending-the-existing-user-model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    fieldsets = [
        (None,               {'fields': ['Username','Password']}),
        ('Personal info',    {'fields': ['first_name']}),
    ]
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# other registrations
admin.site.register(Investigator)
