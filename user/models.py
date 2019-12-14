from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender_choices = (
        ('1', '女性'),
        ('2', '男性'),
        ('3', 'その他'),
        ('4', '選択してください')
    )
    gender = models.CharField(
        max_length=1,
        choices = gender_choices,
        default = 4
        )
    email = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def nickname(self):
        return self.name

    def __str__(self):
        return self.name
