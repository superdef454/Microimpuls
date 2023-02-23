from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name = "tasks"),
    path('<int:id>/<str:status>', views.tasks, name="change")
]