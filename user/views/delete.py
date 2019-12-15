from django.urls import reverse
from django.views.generic import DeleteView
from user.models import User


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/delete.html'

    def get_success_url(self):
        return reverse('list')
