"""
URL configuration for devsearch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # 3
from django.conf.urls.static import static  # 26 функция дает возможность выводить коректно по заданным путям
from django.conf import settings  # 27 путь к нашему документу

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),  # 4 включаем в главный urls все что будет в fourth/devsearch/projects/urls.py
    path('', include('users.urls')),
]

# 28 если сайт в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 29 ОСТАНВАЛИВАЕМ сервер и выполним миграции и создаем суперпользователя
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# теперь мы попадаем в админку и нужно зарегистрировать наши модели что бы они были видны в админке
# закинем картинку default.jpg в корень папки медиа
# далее добавим картинки на сайт,




















