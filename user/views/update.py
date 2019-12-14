from django.urls import reverse
from django.views.generic import UpdateView
from user.forms import UserForm
from user.models import User


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/update.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
