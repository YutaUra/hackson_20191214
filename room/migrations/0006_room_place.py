from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20191214_1853'),
        ('room', '0005_room_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='place',
            field=models.ManyToManyField(blank=True, to='place.Place'),
        ),
    ]
