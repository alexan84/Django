from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    blogs = Blog.objects.order_by('-date')  # сортируем блоги по дате создания
    return render(request, 'blog/blogs.html', {'blogs': blogs})  # это передаем на html страницу


def detail(request, blog_id):  # blog_id это то что пишется в адресной строке после blog и потом передается в путь в  urls.py
    blog = get_object_or_404(Blog, pk=blog_id)  #  если такого айди страницы еще нет то выходит ошибка
    return render(request, 'blog/details.html', {'blog': blog})
