from django.shortcuts import render

def tasks(request):
    out = {
        'Задачи' : [
            {
                "Имя" : "Тест",
                "Описание" : "Тестовое описание",
                "Состояние" : "В работе"
            },
            {
                "Имя" : "Тест 2",
                "Описание" : "Тестовое описание",
                "Состояние" : "Добавлена"
            }
            ],
    }
    return render(request, 'base.html', out)
