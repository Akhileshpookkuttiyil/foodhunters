# Generated by Django 3.2.9 on 2021-12-18 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0002_alter_vlog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlog',
            name='author',
            field=models.CharField(default='unknown', max_length=30),
        ),
        migrations.AddField(
            model_name='vlog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]