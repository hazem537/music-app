# Generated by Django 4.2.7 on 2023-11-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_song_slug_alter_song_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
