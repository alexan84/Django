from django.shortcuts import render, redirect
from .models import Project  # 30
from .forms import ProjectForm  # 37


# 6
def projects(request):
    # 31 получаем данные из класса
    pr = Project.objects.all()
    context = {'projects': pr}
    return render(request, "projects/projects.html", context)


# 32 single_project.html добавляем в корень projects
def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    context = {'project': project_obj}
    return render(request, "projects/single-project.html", context)


# 35 создание проекта
def create_project(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {"form": form}
    return render(request, 'projects/form-template.html', context)  # возвращает страницу которая лежит в папке fourth/devsearch/projects/templates/projects/form-template.html
