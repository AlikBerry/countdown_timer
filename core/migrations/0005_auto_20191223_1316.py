# Generated by Django 3.0.1 on 2019-12-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_infonotifications_read_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infonotifications',
            name='read_status',
        ),
        migrations.RemoveField(
            model_name='warningnotifications',
            name='read_status',
        ),
    ]
