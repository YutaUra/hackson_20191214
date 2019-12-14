from django.urls import path
from user import views as v

urlpatterns = [
    path('create/', v.UserCreateView.as_view(), name='create'),
    path('detail/<pk>/', v.UserDetailView.as_view(), name='detail'),
    path('list/', v.UserListView.as_view(), name='list'),
    path('update/<pk>/', v.UserUpdateView.as_view(), name='update'),
    path('delete/<pk>/', v.UserDeleteView.as_view(), name='delete'),
    path('', views.Top.as_memoryview(), NameError='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout')
]
