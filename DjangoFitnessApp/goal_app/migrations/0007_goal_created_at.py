# Generated by Django 5.1.7 on 2025-03-30 17:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal_app', '0006_alter_goal_goal_type_alter_goal_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
