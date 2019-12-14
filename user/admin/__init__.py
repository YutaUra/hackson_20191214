from django.contrib.admin import site
from .admin import UserAdmin
from user.models import User

site.register(User, UserAdmin)
