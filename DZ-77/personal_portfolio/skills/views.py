from django.shortcuts import render
from .models import Skills


def index(request):
    projects = Skills.objects.all()  # берем все данные из модели скилс,что бы projects увидеть на html странице то передадим его ниже
    return render(request, 'skills/index.html', {'projects': projects})  # подключение html документа,куда и что передаем
