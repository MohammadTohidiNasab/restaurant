from django.shortcuts import render
from . models import Blog,Tag ,Category
# Create your views here.

def blog_page (request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,'blog.html',context)



def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blog=blog)
    recent = Blog.objects.all().order_by('-created_at')[:6]
    category = Category.objects.all()
    context = {
        'blog':blog,
        'tags': tags,
        'recent' : recent,
        'category':category,
    }
    
    return render(request,'blog_details.html',context)
