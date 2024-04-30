# Generated by Django 4.2 on 2024-04-15 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0001_initial'),
        ('user_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewedcontent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='viewedchannel',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_dashboard.channel'),
        ),
        migrations.AddField(
            model_name='viewedchannel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]