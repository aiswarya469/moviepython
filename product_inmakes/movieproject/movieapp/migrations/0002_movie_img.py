# Generated by Django 4.1.1 on 2022-09-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='fdvf', upload_to='gallary'),
            preserve_default=False,
        ),
    ]
