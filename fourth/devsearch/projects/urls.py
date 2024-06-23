# 2
from django.urls import path  # 3
from . import views  # 3

# 4 вынесли для проектов отдельный urls
urlpatterns = [
    path('', views.projects, name='projects'),  # 5
    path('project/<str:pk>', views.project, name='project'),  # 32 путь перебрасывает на страницу проекта при нажатии на проета
    path('create-project/', views.create_project, name='create-project'),  # 34 путь создания проекта
]

























