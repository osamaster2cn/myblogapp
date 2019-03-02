from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

# 記事一覧ページの呼び出し
def index(request):
    posts = Post.objects.order_by('-published')
    title = Post.objects.order_by('-published')
    published = Post.objects.order_by('-published')
    body = Post.objects.order_by('-published')
    # {'Template内での変数名':渡す変数名}
    return render(request, 'posts/index.html',{'posts':posts},)
    return render(request, 'posts/index.html',{'title':title},)
    return render(request, 'posts/index.html',{'published':published},)
    return render(request, 'posts/index.html',{'body':body},)

# 記事詳細ページの呼び出し
def post_detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request, 'posts/post_detail.html',{'post':post})