# Generated by Django 3.2.10 on 2022-02-05 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0005_rename_dob_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Date_of_Birth',
            new_name='dob',
        ),
    ]
