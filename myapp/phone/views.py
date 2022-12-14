from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'phone/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'phone/home.html'
    context_object_name = 'posts'
    ordering =['-date_posted']


def about(request):
    return render (request, 'phone/about.html', {'title':'About'})
