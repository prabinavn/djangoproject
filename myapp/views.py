from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fn_myIndex(request):
    return HttpResponse('Welcome to Django')
def fn_index(request):
    lang=['python','cpp']   
    return render(request,'index.html',{'list1':lang})    
