# Generated by Django 3.2 on 2022-10-18 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='categories',
            new_name='categrories',
        ),
    ]
