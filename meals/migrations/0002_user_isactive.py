# Generated by Django 5.1.2 on 2024-11-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
