# Generated by Django 5.0.6 on 2024-06-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('ip', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, default=None, null=True)),
                ('httpMethod', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('URI', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('responceCode', models.IntegerField(blank=True, default=None, null=True)),
                ('responceSize', models.IntegerField(blank=True, default=None, null=True)),
                ('userAgent', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('hash', models.CharField(default=0, max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]
