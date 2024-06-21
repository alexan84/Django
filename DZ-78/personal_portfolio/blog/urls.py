from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<int:blog_id>', views.detail, name="detail"),  # тут создается динамический путь,который формируется из принимаемого аргументы в адресной строке
    # Авторизация
    path('signup/', views.signupuser, name="signupuser"),
    #
    # Вывод информации
    path('current/', views.currenttodos, name="currenttodos"),
]
