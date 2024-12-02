# Generated by Django 5.1.3 on 2024-11-27 16:17

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('4c5cf833-3eaf-441e-b635-ff605c1699cb'), editable=False, primary_key=True, serialize=False)),
                ('member1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member1_groups', to=settings.AUTH_USER_MODEL)),
                ('member2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member2_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chats.chat')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
