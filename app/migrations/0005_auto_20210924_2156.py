# Generated by Django 3.2.6 on 2021-09-25 04:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_service_servicer_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Querydata1_loc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_type', models.CharField(help_text='Type of query', max_length=50)),
                ('query_detail', models.TextField(help_text='Detail of query')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service_loc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of service', max_length=50)),
                ('provider_name', models.CharField(help_text='Provider name', max_length=50)),
                ('price', models.IntegerField(help_text='Price')),
                ('Servicer_contact', models.CharField(blank=True, default='+91-', help_text='Contact of service provider', max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+91-9999999999'. Up to 10 digits allowed.", regex='[+](0|91)?[-][7-9]\\d{8}')])),
                ('serviceadd_date', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='cover_image/')),
            ],
        ),
        migrations.DeleteModel(
            name='Querydata1',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AddField(
            model_name='querydata1_loc',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queriess', to='app.service_loc'),
        ),
    ]
