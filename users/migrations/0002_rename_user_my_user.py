# Generated by Django 4.1.7 on 2023-04-27 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='my_User',
        ),
    ]
