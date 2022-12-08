from django.shortcuts import render

# Create your views here.

def reserve(request):
    context = {}
    
    return render(request,"reservation.html",context)