from django.shortcuts import render

def home(request):
    context={}
    return render(request,"Myapp/home.html", context)
