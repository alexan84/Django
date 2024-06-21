# 2
from django.urls import path  # 3
from . import views  # 3

# 4 вынесли для проектов отдельный urls
urlpatterns = [
    path('', views.projects, name='projects'),  # 5
]

























