# Generated by Django 4.1.1 on 2022-09-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_remove_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dsbshd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
