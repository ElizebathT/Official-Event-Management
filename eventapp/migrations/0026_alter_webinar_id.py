# Generated by Django 4.2.4 on 2023-10-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0025_alter_webinar_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinar',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
