# Generated by Django 2.2 on 2021-04-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infosite', '0006_auto_20210414_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud_data',
            name='rollno',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]