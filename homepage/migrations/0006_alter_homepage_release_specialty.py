# Generated by Django 4.0.2 on 2022-04-07 14:07

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_op_anaesthesia_type_op_anaesthetist_op_assis1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='release_specialty',
            field=django_mysql.models.ListCharField(models.CharField(max_length=20), max_length=63, size=3),
        ),
    ]
