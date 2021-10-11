# Generated by Django 3.2.6 on 2021-09-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210926_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('price', models.IntegerField(help_text='Price')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='cover_image/')),
            ],
        ),
    ]