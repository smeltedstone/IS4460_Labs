# Generated by Django 5.0.1 on 2024-03-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('director', models.CharField(blank=True, max_length=100)),
                ('release_year', models.CharField(blank=True, max_length=50)),
                ('budget', models.CharField(blank=True, max_length=50)),
                ('runtime', models.CharField(blank=True, max_length=50)),
                ('rating', models.CharField(blank=True, max_length=50)),
                ('genre', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
