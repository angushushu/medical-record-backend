# Generated by Django 4.0.2 on 2022-04-08 16:05

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_alter_homepage_release_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='registered_addr1',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default=None, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AddField(
            model_name='homepage',
            name='registered_addr2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='homepage',
            name='registered_zip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='admit_specialty',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='birthplace',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default=None, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='contact_addr1',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default=None, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='parent_birthplace',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default=None, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='present_addr1',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default=None, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='release_specialty',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='trans_specialty',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='work_addr1',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default=None, max_length=20), default=None, max_length=63, size=3),
        ),
        migrations.AlterField(
            model_name='op',
            name='wound_healing_lvl',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default=None, max_length=20), default=None, max_length=42, size=2),
        ),
    ]