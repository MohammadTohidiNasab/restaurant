from django.shortcuts import render
from . models import Blog,Tag ,Category , Comment
from . forms import CommentForm
from django.core.paginator import Paginator
# Create your views here.

def blog_page (request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,6)
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)
    context = {
        'blog_list':blog_list
    }
    return render(request,'blog.html',context)




def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blog=blog)
    recent = Blog.objects.all().order_by('-created_at')[:6]
    category = Category.objects.all()
    comments = Comment.objects.all().filter(blog=blog)
    
    if  request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_emai = form.cleaned_data['email']
            new_mesagge = form.cleaned_data['message']
            
            new_comment = Comment(blog=blog,name=new_name,email=new_emai,massage=new_mesagge)
            new_comment.save()
    context = {
        'blog':blog,
        'tags': tags,
        'recent' : recent,
        'category':category,
        'comments' : comments,
    }
    
    return render(request,'blog_details.html',context)

def blog_tag(request,tag):
    blogs = Blog.objects.filter(tags__slug=tag)
    context = {
        'blogs': blogs
    }
    return render(request,'blog/blog.html',context)



def blog_category(request,category):
    
    blogs = Blog.objects.filter(category__slug=category)
                                    
    context = {
        'blogs': blogs
    }
    
    return render(request,'blog/blog.html',context)
