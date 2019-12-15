from django.urls import path
from user import views as v

app_name = 'user'
urlpatterns = [
    path('create/', v.UserCreateView.as_view(), name='create'),
    path('detail/<pk>/', v.UserDetailView.as_view(), name='detail'),
    path('list/', v.UserListView.as_view(), name='list'),
    path('update/<pk>/', v.UserUpdateView.as_view(), name='update'),
    path('delete/<pk>/', v.UserDeleteView.as_view(), name='delete'),
    path('login/', v.Login.as_view(), name='login'),
    path('logout/', v.Logout.as_view(), name='logout')
]
