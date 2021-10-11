# Generated by Django 3.2.6 on 2021-09-29 01:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_post_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='provider_contact',
            field=models.CharField(blank=True, default='+91-', max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+91-9999999999'. Up to 10 digits allowed.", regex='[+](0|91)?[-][7-9]\\d{8}')]),
        ),
        migrations.AlterField(
            model_name='postquery',
            name='query_detail',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='postquery',
            name='query_type',
            field=models.CharField(max_length=50),
        ),
    ]