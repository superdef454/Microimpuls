from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Task

admin.site.register(Task)

admin.site.site_title = 'Планировщик задач'
admin.site.site_header = 'Планировщик задач'

class AccessUser(object):
    has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True

admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True

# We add this to remove the user/group admin in the admin site as there is no user authentication
admin.site.unregister(User)
admin.site.unregister(Group)

# Create superuser for admin use in case it doesn't exist
try:
    User.objects.get_by_natural_key('admin')
except User.DoesNotExist:
    User.objects.create_superuser('admin', '', 'admin')
