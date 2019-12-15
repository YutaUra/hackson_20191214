from django.urls import path
from room import views as v

app_name = 'room'
urlpatterns = [
    path('create/', v.RoomCreateView.as_view(), name='create'),
    path('detail/<pk>/', v.RoomDetailView.as_view(), name='detail'),
    path('list/', v.RoomListView.as_view(), name='list'),
    path('update/<pk>/', v.RoomUpdateView.as_view(), name='update'),
    path('delete/<pk>/', v.RoomDeleteView.as_view(), name='delete'),
    path('join/<room_pk>/', v.JoinView.as_view(), name='join'),
]
