from django.shortcuts import render

from .models import Task

def tasks(request):
    # print(request.GET.get("Title"), request.GET.get("description"), request.GET.get("status"))
    # Tasks = Task.objects.all()
    # out = {"Задачи" : []}
    # for i in Tasks:
    #     out["Задачи"].append({
    #         "Имя" : i.title,
    #         "Описание" : i.description,
    #         "Состояние": i.status.title(),
    #         "Время" : "22.22.22" #i.create_dateTime.date().strftime()
    #     })
    out = {
        'Задачи' : [
            {
                "Имя" : "Тест",
                "Описание" : "Тестовое описание",
                "Состояние" : "В работе",
                "Время" : "22.12.23"
            },
            {
                "Имя" : "Тест 2",
                "Описание" : "Тестовое описание",
                "Состояние" : "Добавлена",
                "Время" : "22.12.23"
            },
            {
                "Имя" : "Тест 3",
                "Описание" : "Тестовое описание",
                "Состояние" : "Выполнена",
                "Время" : "22.12.23"
            },
            {
                "Имя" : "Тест",
                "Описание" : "Тестовое описание",
                "Состояние" : "В работе",
                "Время" : "22.12.23"
            },
            {
                "Имя" : "Тест 2",
                "Описание" : "Тестовое описание",
                "Состояние" : "Добавлена",
                "Время" : "22.12.23"
            },
            ],
    }
    print(*out["Задачи"])
    return render(request, 'index.html', out)