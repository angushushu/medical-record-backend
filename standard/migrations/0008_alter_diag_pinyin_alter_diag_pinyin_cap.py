# Generated by Django 4.0.2 on 2022-07-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0007_rename_spstd_applieddgstd_dgstd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diag',
            name='pinyin',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='diag',
            name='pinyin_cap',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]