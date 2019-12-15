from django.urls import reverse
from django.views.generic import CreateView
from user.forms import UserForm
from user.models import User
from django.contrib.auth import login


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'

    def get_success_url(self):
        return reverse('user:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        user = form.save(commit=True)
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)
