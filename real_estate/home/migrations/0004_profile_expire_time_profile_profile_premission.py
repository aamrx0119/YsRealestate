# Generated by Django 4.0.2 on 2022-03-08 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_profile_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='expire_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_premission',
            field=models.CharField(choices=[('Gold', 'Gold'), ('Basic', 'Basic')], default='Basic', max_length=5),
        ),
    ]
