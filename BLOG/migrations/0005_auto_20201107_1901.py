# Generated by Django 3.1.2 on 2020-11-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0004_auto_20201107_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_self_anime',
            name='PRF_profile_image',
            field=models.ImageField(upload_to=''),
        ),
    ]