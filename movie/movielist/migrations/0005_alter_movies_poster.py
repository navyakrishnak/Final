# Generated by Django 5.0.1 on 2024-03-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0004_alter_movies_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster',
            field=models.ImageField(blank=True, upload_to='moviepotser'),
        ),
    ]
