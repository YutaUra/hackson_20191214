from django.views.generic import ListView
from user.models import User


class UserListView(ListView):
    model = User
    template_name = 'user/list.html'
