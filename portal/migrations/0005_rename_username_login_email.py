# Generated by Django 4.2.5 on 2023-10-14 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_registration_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='username',
            new_name='email',
        ),
    ]