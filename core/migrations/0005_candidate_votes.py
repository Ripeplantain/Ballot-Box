# Generated by Django 4.1.4 on 2023-02-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profile_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
