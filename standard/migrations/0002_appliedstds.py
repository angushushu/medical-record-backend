# Generated by Django 4.0.2 on 2022-04-22 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedStds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spstd', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applied_stds', to='standard.specialtystd')),
            ],
        ),
    ]
