from django.db import models
from users.models import Profile


# 22 создадим две модели на основе которых создаются таблицы в БД

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # описание проекта, не обязательно
    featured_image = models.ImageField(default="default.jpg",
                                       upload_to="projects/%Y/%m/%d")  # создает папку в медиа projects если картинки нет то заполним ее значением по умолчанию, если картинка есть токуда будет сохранятся
    demo_link = models.CharField(max_length=2000, blank=True)
    source_link = models.CharField(max_length=2000, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)  # свяжем две наших модели
    vote_total = models.IntegerField(default=0)  # процент отзывов, целочисленное значение, если не указанно то по умолчанию 0
    vote_ratio = models.IntegerField(default=0)  # процент относительно всех голосов будет положительно
    created = models.DateTimeField(auto_now_add=True)  # дата создания тега,в момент создания какого то проекта

    def __str__(self):
        return self.title


# 23
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)  # дата создания тега,в момент создания какого то проекта

    def __str__(self):
        return self.name
