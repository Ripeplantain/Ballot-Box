# Generated by Django 4.1.4 on 2023-03-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_profile_created_at_profile_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=models.ImageField(blank=True, upload_to='candidate_pics/'),
        ),
    ]