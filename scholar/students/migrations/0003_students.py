# Generated by Django 4.2.6 on 2023-11-08 00:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_user_created_at_user_deleted_at_user_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('id_person', models.IntegerField()),
                ('status', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('update_at', models.DateTimeField(default=datetime.datetime.now)),
                ('deleted_at', models.DateField(null=True)),
            ],
        ),
    ]
