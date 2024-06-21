from django.shortcuts import render


# 6
def projects(request):
    return render(request, "projects/projects.html")
