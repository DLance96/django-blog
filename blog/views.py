from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post(request, post_id):
    posts = Post.objects.filter(pk=post_id)
    return render(request, 'blog/post_list.html', {'posts':posts})

def year_archive(request, year):
    posts = Post.objects.filter(pub_date__year = year).order_by('pub_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def month_archive(request, year, month):
    posts = Post.objects.filter(pub_date__month = month, pub_date__year = year).order_by('pub_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
