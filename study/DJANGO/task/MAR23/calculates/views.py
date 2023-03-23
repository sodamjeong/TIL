from django.shortcuts import render

# Create your views here.

def calpage(request):
    return render(request, 'calculates.html')

def calculate(request,number1,number2):
        context = {
        'plus' : number1 + number2,
        'minus' : number1 - number2,
        'multi' : number1 * number2,
        'div' : number1 // number2,
    }
        return render(request, 'calculate.html', context)

def calculate_plus(request):

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    context = {
        'plusnum' : int(num1) + int(num2)
    }
    return render(request, 'calculate_plus.html', context)

def calculate_minus(request):

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    context = {
        'minusnum' : int(num1) - int(num2)
    }
    return render(request, 'calculate_minus.html', context)

def calculate_multi(request):

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    context = {
        'multinum' : int(num1) * int(num2)
    }
    return render(request, 'calculate_multi.html', context)

def calculate_div(request):

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    context = {
        'divnum' : int(num1) // int(num2)
    }
    return render(request, 'calculate_div.html', context)