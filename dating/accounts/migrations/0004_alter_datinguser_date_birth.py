# Generated by Django 5.1.3 on 2024-11-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_datinguser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datinguser',
            name='date_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]