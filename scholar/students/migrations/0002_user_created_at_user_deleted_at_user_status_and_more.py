# Generated by Django 4.2.6 on 2023-11-08 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
