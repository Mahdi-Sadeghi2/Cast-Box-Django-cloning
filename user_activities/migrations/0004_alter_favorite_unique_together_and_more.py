# Generated by Django 4.2 on 2024-04-19 09:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_activities', '0003_playlist_podcasts'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'episode')},
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'episode')},
        ),
        migrations.AlterUniqueTogether(
            name='watchhistory',
            unique_together={('user', 'episode')},
        ),
    ]
