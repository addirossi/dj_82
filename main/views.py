from django.shortcuts import render
from django.http import HttpResponse

from main.models import Category, Post


def index(request):
    return HttpResponse('Hello! This is a test response message')


def categories_list(request):
    categories = Category.objects.all()
    template_name = 'main/categories.html'
    print(f'FFFFFFF!!!!: {categories}')
    return render(request, template_name, {'categories_list': category})


def posts_list_by_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    template_name = 'main/posts.html'
    return render(request, template_name, {'posts': posts})
