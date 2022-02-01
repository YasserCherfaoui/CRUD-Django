from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
# Create your views here.


def index(request):
    data = Post.objects.all()
    return render(request=request, template_name='main/index.html', context={'data': data})


def read(request, post_id):
    if post_id:
        post = Post.objects.filter(pk=post_id)

    return render(request=request, template_name='main/read.html', context={'post': post.get()})


def update(request, post_id):
    if post_id:
        post = Post.objects.filter(pk=post_id)
    if request.POST:
        n_t = request.POST['title']
        n_c = request.POST['content']
        post.update(title=n_t, content=n_c)
        return redirect('/')
    return render(request=request, template_name='main/update.html', context={'post': post.get()})


def delete(request, post_id):
    if post_id:
        p = Post.objects.filter(pk=post_id)
        p.delete()
        return HttpResponse('Post has been successfully deleted')
    return HttpResponse('insert a post id to delete')


def create(request):
    if request.POST:
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('/')
    return render(request=request, template_name='main/create.html', context={})
