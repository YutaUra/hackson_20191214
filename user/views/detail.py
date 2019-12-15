from django.views.generic import DetailView
from user.models import User


class UserDetailView(DetailView):
    model = User
    template_name = 'user/detail.html'
