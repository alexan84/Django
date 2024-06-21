from django.db import models

# создадим класс создающий таблицу в БД


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    # возвращает строковое значение,тут выводятся заголовки статей при обращении к экземпляру класса блог
    def __str__(self):
        return self.title

