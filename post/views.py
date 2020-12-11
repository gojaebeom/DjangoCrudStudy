from post.models import Post
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'post/index.html', context={'post_list':post_list})

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/show.html', context={'post':post})

def create(request):
    return render(request, 'post/create.html')

def store(request):
    post = Post()
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('/posts')

def update(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/update.html', context={'post':post})

def edit(request, id):
    post = Post.objects.get(id=id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()

    return redirect('/posts')

def destroy(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/posts')