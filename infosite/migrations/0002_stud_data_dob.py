# Generated by Django 2.2 on 2021-04-01 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infosite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud_data',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]