# Generated by Django 3.2.6 on 2021-09-29 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20210928_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='provider',
            field=models.CharField(max_length=100),
        ),
    ]
