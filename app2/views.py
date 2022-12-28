from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string2(request):
    return HttpResponse('this is string2 function of app2')

def second(request):
        return render(request,'second.html')