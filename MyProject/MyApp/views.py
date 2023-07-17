from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
	return HttpResponse("hello world")

def task(request,id,name):
	return HttpResponse("My Rollnumber is {} and my name is {}".format(id,name))

def temp(request):
	return render(request,'MyApp/temp.html',{})

def table(request):
	return render(request,'MyApp/table.html')