# Generated by Django 4.2.4 on 2024-03-04 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0057_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.service'),
        ),
    ]
