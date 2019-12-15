# Generated by Django 3.0 on 2019-12-14 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0003_auto_20191214_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='participant',
            field=models.ManyToManyField(blank=True, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]