# Generated by Django 3.1.2 on 2020-11-07 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0008_comment_self_anime_testing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_self_anime',
            name='testing',
        ),
    ]
