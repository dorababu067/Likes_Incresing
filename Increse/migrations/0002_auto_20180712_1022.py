# Generated by Django 2.0.4 on 2018-07-12 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Increse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='posts',
            new_name='votes',
        ),
    ]