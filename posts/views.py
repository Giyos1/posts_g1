from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def home(request):
    return render(request, 'index.html')

def posts(request):
    posts = Post.published_posts.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context=context)

def post_details(request, pk):
    if pk:
        post = Post.published_posts.filter(pk=pk).first()

        data = {
            'post': post
        }

        return render(request, 'post_details.html', context=data)
    return redirect('home')

def post_edit(request, pk):
    if request.method == 'POST':
        if pk:
            title = request.POST.get('title')
            slug = request.POST.get('slug')
            body = request.POST.get('body')
            status = request.POST.get('status')

            Post.published_posts.filter(pk=pk).update(
                title=title,
                slug=slug,
                body=body,
                status=status
            )
            return redirect('posts')
        else:
            return redirect('posts')
    if pk:
        post = Post.published_posts.filter(pk=pk).first()
        print(pk, post)
        data = {
            'post': post
        }
        return render(request, 'post_edit.html', context=data)

def post_delete(request, pk):
    if pk:
        Post.published_posts.filter(pk=pk).update(is_deleted=True)

        return redirect('posts')
    return redirect('home')

