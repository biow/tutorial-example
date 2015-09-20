from datetime import datetime

from django.shortcuts import render

from trips.models import Post

from .forms import PostForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404


def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()})


def home(request):
    # get all the posts
    post_list = Post.objects.all()
    return render(request,
                  'home.html',
                  {'post_list': post_list})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.aurhor = request.user
            post.save()
            return redirect('trips.views.post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('trips.views.post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
