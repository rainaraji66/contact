from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import render , redirect


posts = [
    {
        
        'title': 'Welcome to Home',
        'content': 'By Raji',
        'date_posted': 'Oct 9, 2022'
        
    }
    
]


def home(request):

    context = {
        'posts': posts
    }
    
    return render(request,'crud/home.html',context) 

def about(request):
    return render(request, 'crud/about.html', {'title': 'About'})



    

