from django.shortcuts import render

# Create your views here.
def myfunc(request):
    return render(request,'index.html',{})
