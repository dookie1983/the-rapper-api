# Generated by Django 3.2.2 on 2021-05-09 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='single',
            old_name='views',
            new_name='youtube_views',
        ),
    ]
