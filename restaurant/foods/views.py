from django.shortcuts import render
from .models import Foods
# Create your views here.

def food_list(request):
    food_list = Foods.objects.all()
    context= {
        "foods" : food_list
              }
    
    return render (request,'foods/list.html',context)
