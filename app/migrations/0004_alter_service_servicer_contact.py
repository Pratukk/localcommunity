# Generated by Django 3.2.6 on 2021-09-23 11:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_service_servicer_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Servicer_contact',
            field=models.CharField(blank=True, default='+91-', help_text='Contact of service provider', max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='[+](0|91)?[-][7-9]\\d{8}')]),
        ),
    ]
