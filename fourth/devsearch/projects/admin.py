from django.contrib import admin
from .models import Project, Tag
# 30 регистрируем модели и они появляются в админке

admin.site.register(Project)
admin.site.register(Tag)
