# Generated by Django 4.1.7 on 2023-02-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Добавлена', 'Добавлена'), ('В Работе', 'В Работе'), ('Выполнена', 'Выполнена')], default='Добавлена', max_length=15, verbose_name='Статус задачи'),
        ),
    ]
