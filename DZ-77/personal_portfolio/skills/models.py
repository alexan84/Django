from django.db import models
# что бы этот класс понимал что он в будующем должен стать таблицей в БД вставляем в скобки models.Model, по умолчанию все поля обязательны для заполнения


class Skills(models.Model):
    title = models.CharField(max_length=100)  # навыки разраба - тут тип данных из джанго
    description = models.CharField(max_length=250)  # описание
    image = models.ImageField(upload_to='skills/images/')  # путь где хранится изображение
    url = models.URLField(blank=True)  # поле не обязательно для заполнения

    # возвращает строковое значение,тут выводятся заголовки статей при обращении к экземпляру класса блог
    def __str__(self):
        return self.title