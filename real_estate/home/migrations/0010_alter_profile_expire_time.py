# Generated by Django 4.0.2 on 2022-03-18 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expire_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
