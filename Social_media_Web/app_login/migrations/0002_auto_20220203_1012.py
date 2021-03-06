# Generated by Django 3.2.10 on 2022-02-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='feacbook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
