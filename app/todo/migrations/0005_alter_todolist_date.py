# Generated by Django 4.1.6 on 2023-04-19 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_users_profile_photo_alter_todolist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 19, 15, 46, 15, 539985, tzinfo=datetime.timezone.utc)),
        ),
    ]
