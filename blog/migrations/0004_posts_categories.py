# Generated by Django 3.2 on 2022-10-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_posts_categrories'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='categories',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]