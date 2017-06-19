from django.shortcuts import render, redirect
import random
# Create your views here.

def isPrime(number):
    if number ==1 :
        return True
    for i in range(2, number):
        if number % 1 == 0:
            return False

def index(request):
    return render(request, 'landscapes_app/index.html')

def process(request, number):
    number = int(str(number))
    
    if isPrime(number):
        randomnum = random.randint(0,5)
        list =['static/landscape_app/img/snow.jpg', 'static/landscapes_app/img/desert.jpg', 'static/landscapes_app/img/forest.jpg', 'static/landscapes_app/img/vineyard.jpg', 'static/landscapes_app/img/tropical.jpg']
        src = list[randomnum]
    elif number <= 10:
        src = 'static/landscapes_app/img/snow.jpg'
    elif number <= 20:
        src = 'static/landscapes_app/img/desert.jpg'
    elif number <= 30:
        src = 'static/landscapes_app/img/forest.jpg'
    elif number <= 40:
        src = 'static/landscapes_app/img/vineyard.jpg'
    elif number <= 50:
        src = 'static/landscapes_app/img/tropical.jpg'
    else: 
        return redirect('/')

    context = {
        "src" : src
    }

    return render(request, 'landscapes_app/show.html', context)
    