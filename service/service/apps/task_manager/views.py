from django.shortcuts import render

from .models import Task

def tasks(request, id: int = -1, status: str = None):
    if id >= 0 and status:
        if Task.objects.filter(id=id).exists():
            task = Task.objects.get(id=id)
            if status == Task.ADD or status == Task.END or status == Task.WORKED:
                task.status = status
                task.save()
            if status == "Удалить":
                task.delete()
    if request.GET.get("Title") and request.GET.get("description") and request.GET.get("status"):
        if not Task.objects.filter(title=request.GET.get("Title")).exists():
            Task.objects.create(title=request.GET.get("Title"), description = request.GET.get("description"), status = request.GET.get("status"))
    Tasks = Task.objects.all()
    out = {"Задачи" : []}
    for i in Tasks:
        out["Задачи"].append({
            "Имя" : i.title,
            "Описание" : i.description,
            "Состояние": i.status.title(),
            "id": i.id,
            "Время" : i.create_dateTime,
        })
    return render(request, 'index.html', out)

def changeStatus(request):
    Tasks = Task.objects.all()
    out = {"Задачи" : []}
    for i in Tasks:
        out["Задачи"].append({
            "Имя" : i.title,
            "Описание" : i.description,
            "Состояние": i.status.title(),
            "id": i.id,
            "Время" : i.create_dateTime,
        })
    return render(request, 'index.html', out)