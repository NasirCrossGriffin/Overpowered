# Generated by Django 5.2.1 on 2025-05-19 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_exercise_distance_remove_exercise_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='workout',
        ),
        migrations.RemoveField(
            model_name='set',
            name='exercise',
        ),
        migrations.CreateModel(
            name='User_Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.workout')),
            ],
        ),
        migrations.AddField(
            model_name='set',
            name='user_exercise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.user_exercise'),
            preserve_default=False,
        ),
    ]
