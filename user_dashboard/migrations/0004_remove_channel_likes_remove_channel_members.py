# Generated by Django 4.2 on 2024-04-20 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0003_alter_channel_episode_count_subscriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='members',
        ),
    ]
