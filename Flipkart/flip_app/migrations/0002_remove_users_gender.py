# Generated by Django 4.1.3 on 2022-11-07 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flip_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='Gender',
        ),
    ]
