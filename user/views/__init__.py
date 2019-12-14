from .create import UserCreateView
from .detail import UserDetailView
from .list import UserListView
from .update import UserUpdateView
from .delete import UserDeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.view import generic
from .forms import LoginForm

class Top(generic.TemplateView):
    template_name = 'register/top.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/top.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'register/top.html'

