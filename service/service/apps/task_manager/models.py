from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
class Task(models.Model):
    # Типы статусов:
    ADD = "Добавлена"
    WORKED = "В Работе"
    END = "Выполнена"
    CHOISE_STATUS = [
        (ADD, "Добавлена"),
        (WORKED, "В Работе"),
        (END, "Выполнена")
    ]
    title = models.CharField('Название задачи', max_length=100)
    description = models.TextField('Описание задачи', null=False)
    status = models.CharField('Статус задачи', max_length=15, choices=CHOISE_STATUS, default=ADD)
    create_dateTime = models.DateTimeField("Время создания Задачи", auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
