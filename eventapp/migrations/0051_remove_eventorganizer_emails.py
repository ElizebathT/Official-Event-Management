# Generated by Django 4.2.4 on 2024-02-09 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0050_remove_service_booked_dates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventorganizer',
            name='emails',
        ),
    ]
