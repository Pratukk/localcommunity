# Generated by Django 3.2.6 on 2021-09-25 18:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_alter_query_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='creator',
        ),
        migrations.AddField(
            model_name='query',
            name='creator',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]