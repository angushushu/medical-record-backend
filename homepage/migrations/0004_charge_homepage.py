# Generated by Django 4.0.2 on 2022-04-01 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='homepage',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='charge', to='homepage.homepage'),
        ),
    ]
