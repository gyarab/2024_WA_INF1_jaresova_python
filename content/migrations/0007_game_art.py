# Generated by Django 5.1.4 on 2025-05-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_alter_comment_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='art',
            field=models.ImageField(blank=True, null=True, upload_to='art'),
        ),
    ]
