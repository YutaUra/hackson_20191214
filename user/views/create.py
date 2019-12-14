from django.urls import reverse
from django.views.generic import CreateView
from user.forms import UserForm
from user.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
