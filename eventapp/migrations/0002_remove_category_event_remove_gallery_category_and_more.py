# Generated by Django 5.1.4 on 2024-12-16 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='event',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='category',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
