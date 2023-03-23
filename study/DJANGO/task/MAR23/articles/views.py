from django.shortcuts import render

# Create your views here.

def main(request):
    return render (request, 'main.html')

def printpage(request):
    return render(request,'printpage.html')

def throw(request):
    return render (request, 'throw.html')

def catch(request):
    data = request.GET.get('content')
    context = {
        'data' : data,
    }
    return render(request, 'catch.html', context)

def number_print(request, number):
    context = {
        'number' : number,
    }
    return render(request, 'number_print.html', context)
