# Generated by Django 4.1.6 on 2023-04-19 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todolist_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile_photo',
            field=models.ImageField(default='app/images/empty.webp', upload_to='app/images'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 19, 15, 42, 19, 279578, tzinfo=datetime.timezone.utc)),
        ),
    ]
