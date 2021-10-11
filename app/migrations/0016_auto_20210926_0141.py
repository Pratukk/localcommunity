# Generated by Django 3.2.6 on 2021-09-26 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0015_auto_20210926_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_type', models.CharField(help_text='Type of query', max_length=50)),
                ('query_detail', models.TextField(help_text='Detail of query')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service_loc')),
            ],
        ),
        migrations.DeleteModel(
            name='Query',
        ),
    ]