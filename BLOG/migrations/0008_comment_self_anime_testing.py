# Generated by Django 3.1.2 on 2020-11-07 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201107_1909'),
        ('BLOG', '0007_comment_self_anime_prf_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_self_anime',
            name='testing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
            preserve_default=False,
        ),
    ]
