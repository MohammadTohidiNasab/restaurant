from django.shortcuts import render
from .models import Foods
# Create your views here.

def food_list(request):
    food_list = Foods.objects.all()
    context= {
        "foods" : food_list
              }
    
    return render (request,'foods/list.html',context)


def food_detail(requste,id):
    food = Foods.objects.get(id = id)
    
    context = {
        'food': food
    }
    
    return render(requste,'foods/detail.html',context)

