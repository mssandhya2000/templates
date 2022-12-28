from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string1(request):
    return HttpResponse('<h1>this is string1 function of app1</h1>')

def first(request):
    return render(request,'first.html')