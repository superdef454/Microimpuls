# Generated by Django 4.1.7 on 2023-02-22 20:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='create_dateTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания Задачи'),
            preserve_default=False,
        ),
    ]
