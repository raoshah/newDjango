from django.shortcuts import render
from .models import Post, Question, Youtube

def home(request):
    post = Post.objects.all()
    que = Question.objects.all()
    videos = Youtube.objects.all()
    qnum = 0
    z = que[qnum]
    qnum = qnum + 1
    return render(request, "myapp/home.html", {
        "post": post,
        "z": z,
        "q": qnum,
        "videos": videos
    })