from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #Excercise 3 added the <a... part
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")#, 'rango/index.html')



#Excersis 3: Added the <a... part and the about part
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>.")



