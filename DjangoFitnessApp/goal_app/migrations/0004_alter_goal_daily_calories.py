# Generated by Django 5.1.7 on 2025-03-29 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal_app', '0003_goal_daily_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='daily_calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
