# Generated by Django 4.1.6 on 2023-03-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='passed',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
