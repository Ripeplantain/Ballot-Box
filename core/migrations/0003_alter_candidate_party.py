# Generated by Django 4.1.4 on 2023-02-24 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_party_alter_candidate_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.party'),
        ),
    ]
