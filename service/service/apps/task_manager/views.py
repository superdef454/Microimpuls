from django.shortcuts import render
from django.utils import timezone
import pytz


from .models import Task

def tasks(request, id: int = -1, status: str = None):
    # Разбор изменения статуса задачи
    if id >= 0 and status:
        if Task.objects.filter(id=id).exists():
            task = Task.objects.get(id=id)
            if status == Task.ADD or status == Task.END or status == Task.WORKED:
                task.status = status
                task.save()
            if status == "Удалить":
                task.delete()
    # Добавление новой и проверка на наличие добовляемой записи в БД
    if request.GET.get("Title") and request.GET.get("description") and request.GET.get("status"):
        if not Task.objects.filter(title=request.GET.get("Title")).exists():
            Task.objects.create(title=request.GET.get("Title"), description = request.GET.get("description"), status = request.GET.get("status"))
    # Я понимаю, что часть функционала нужно разнести по разным функциям и путям, но время мало
    out = {"Задачи" : []}
    # Для корректного определения времени
    current_tz = pytz.timezone('Asia/Yekaterinburg')
    timezone.activate(current_tz)
    # Была попытка объединить 3 запроса в один
    # Tasks = Task.objects.filter(status=Task.WORKED).union(Task.objects.filter(status=Task.ADD)).union(Task.objects.filter(status=Task.END))
    # или так
    # from django.db.models import Q
    # Tasks = Task.objects.filter(Q(status=Task.WORKED) and Q(status=Task.ADD) and Q(status=Task.END))
    # или так
    # work = Task.objects.filter(status=Task.WORKED)
    # add = Task.objects.filter(status=Task.ADD)
    # end = Task.objects.filter(status=Task.END)
    # Tasks = work | add | end 
    # Но все не то, поэтому поочерёдные запросы
    Tasks = Task.objects.filter(status=Task.WORKED)
    for i in Tasks:
        out["Задачи"].append({
            "Имя" : i.title,
            "Описание" : i.description,
            "Состояние": i.status.title(),
            "id": i.id,
            "Время" : i.create_dateTime,
        })
    Tasks = Task.objects.filter(status=Task.ADD)
    for i in Tasks:
        out["Задачи"].append({
            "Имя" : i.title,
            "Описание" : i.description,
            "Состояние": i.status.title(),
            "id": i.id,
            "Время" : i.create_dateTime,
        })
    Tasks = Task.objects.filter(status=Task.END)
    for i in Tasks:
        out["Задачи"].append({
            "Имя" : i.title,
            "Описание" : i.description,
            "Состояние": i.status.title(),
            "id": i.id,
            "Время" : i.create_dateTime,
        })
    return render(request, 'index.html', out)