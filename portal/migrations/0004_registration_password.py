# Generated by Django 4.2.5 on 2023-10-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_registration_address_registration_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
