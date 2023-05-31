# Generated by Django 4.2.1 on 2023-05-31 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('person', models.IntegerField(null=True)),
                ('match', models.IntegerField(default=0, null=True)),
                ('reciverphone', models.CharField(blank=True, max_length=30, null=True)),
                ('postphone', models.CharField(blank=True, max_length=30, null=True)),
                ('recivertext', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, default=0, null=True)),
                ('lan', models.FloatField(blank=True, default=0, null=True)),
                ('postuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_sent', to=settings.AUTH_USER_MODEL)),
                ('reciveuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
