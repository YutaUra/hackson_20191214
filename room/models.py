from django.db import models
from django.contrib.auth import get_user_model
from place.models import Filter

User = get_user_model()


class Room(Filter):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='owner')
    participant = models.ManyToManyField(to=User, related_name='participant',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name
