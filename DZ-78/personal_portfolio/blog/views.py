from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def blogs(request):
    blogs = Blog.objects.order_by('-date')  # сортируем блоги по дате создания
    return render(request, 'blog/blogs.html', {'blogs': blogs})  # это передаем на html страницу


def detail(request, blog_id):  # blog_id это то что пишется в адресной строке после blog и потом передается в путь в  urls.py
    blog = get_object_or_404(Blog, pk=blog_id)  #  если такого айди страницы еще нет то выходит ошибка
    return render(request, 'blog/details.html', {'blog': blog})


def signupuser(request):
    if request.method == "GET":
        return render(request, 'blog/signupuser.html',{'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'blog/signupuser.html',
                              {'form': UserCreationForm(), 'error': "Такое имя пользователя уже существует"})
        else:
            return render(request, 'blog/signupuser.html',{'form': UserCreationForm(), 'error': "Пароли не совпадают"})


def currenttodos(request):
    return render(request, 'blog/currenttodos.html')