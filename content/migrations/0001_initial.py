# Generated by Django 5.1.4 on 2025-01-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('perex', models.TextField(max_length=200)),
                ('text', models.TextField()),
                ('published', models.DateTimeField()),
            ],
        ),
    ]
