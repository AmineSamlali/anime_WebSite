# Generated by Django 3.1.2 on 2020-11-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0006_remove_comment_self_anime_prf_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_self_anime',
            name='PRF_profile_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
