# Generated by Django 5.1.3 on 2024-11-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datinguser',
            name='Interests',
            field=models.ManyToManyField(related_name='users', to='accounts.interst'),
        ),
    ]