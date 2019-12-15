from django.urls import reverse

from .create import UserCreateView
from .detail import UserDetailView
from .list import UserListView
from .update import UserUpdateView
from .delete import UserDeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from user.forms import LoginForm


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse('room:list')


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'user/login.html'
