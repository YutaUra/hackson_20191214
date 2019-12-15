# Generated by Django 3.0 on 2019-12-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('1', '女性'), ('2', '男性'), ('3', 'その他'), ('4', '選択してください')], default=4, max_length=1),
        ),
    ]
