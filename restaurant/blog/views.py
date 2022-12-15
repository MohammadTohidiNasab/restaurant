from django.shortcuts import render
from . models import Blog
# Create your views here.

def blog_page (request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,'blog.html',context)



def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog':blog
    }
    
    return render(request,'blog_details.html',context)
