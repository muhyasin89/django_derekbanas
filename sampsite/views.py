from django.http import HttpResponse


import random

def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("wel this is  Home Page")

def random_number(request, max_number=100):
    random_num =  random.randrange(0, int(max_number))

    msg = "Random number between 0 and  %s : %d " %(max_number,random_num)

    return HttpResponse(msg)