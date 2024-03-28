# Generated by Django 5.0.1 on 2024-03-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('movieName', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=2)),
                ('review', models.CharField(max_length=100)),
            ],
        ),
    ]
