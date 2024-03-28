# Generated by Django 5.0.1 on 2024-03-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('poster', models.ImageField(upload_to='movieposter')),
                ('desc', models.CharField(max_length=100)),
                ('releaseDate', models.DateField()),
                ('youtubelink', models.URLField()),
                ('username', models.CharField(max_length=30)),
                ('actors', models.TextField(max_length=100)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]
