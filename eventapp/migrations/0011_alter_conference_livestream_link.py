# Generated by Django 4.2.4 on 2023-09-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0010_alter_conference_livestream_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='livestream_link',
            field=models.URLField(blank=True, default=None),
        ),
    ]
