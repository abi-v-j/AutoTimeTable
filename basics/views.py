from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method == "POST":
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        s=num1 + num2
        return render(request,'basics/add.html',{'result':s})
    else:
        return render(request,'basics/add.html')

def largest(request):
    if request.method == "POST":
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        num3 = int(request.POST.get('num3'))
        if num1>num2 and num1>num3:
            return render(request,'basics/largest.html',{'result':num1})
        elif num2>num1 and num2>num3:
            return render(request,'basics/largest.html',{'result':num2})
        else:
            return render(request,'basics/largest.html',{'result':num3})
    else:
        return render(request,'basics/largest.html')