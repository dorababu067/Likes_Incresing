from django.shortcuts import render,HttpResponse
from .models import Posts,Like
# Create your views here.

def home_view(request):
    post = Posts.objects.all()
    return render(request,'home.html',{'all':post})

def likes_view(request,id =None):
    if request.method == "GET":
        liked_post = Posts.objects.filter(id=id).get()
        obj = Like(posts = liked_post)
        obj.save()
        likes = liked_post.like_set.all().count()
        #post = Posts.objects.all()
        return render(request,'home.html',{'likes':likes})
