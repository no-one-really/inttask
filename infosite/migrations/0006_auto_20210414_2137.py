# Generated by Django 2.2 on 2021-04-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infosite', '0005_auto_20210413_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud_data',
            name='student_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
