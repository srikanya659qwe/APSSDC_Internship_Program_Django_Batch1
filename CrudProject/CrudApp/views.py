from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrudApp.models import Student
from CrudApp.forms import StudentForm
from CrudProject import settings
from django.core.mail import send_mail
# Create your views here.

def sample(request):
	return render(request,'CrudApp/sample.html')

def insert(request):
	if request.method=="POST":
		na=request.POST['uname']
		roll=request.POST['rnm']
		age=request.POST['age']
		mb=request.POST['mbl']
		em=request.POST['email']
		add=request.POST['addr']

		Student.objects.create(name=na,rollnum=roll,age=age,
			mobile=mb,email=em,address=add)

		# return HttpResponse("Your data is inserted succssfully")
		return redirect('/read')

	return render(request,'CrudApp/insert.html')


def read(request):
	data=Student.objects.all()
	return render(request,'CrudApp/read.html',{'data':data})

def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.name=request.POST['uname']
		data.rollnum=request.POST['rnm']
		data.age=request.POST['age']
		data.mobile=request.POST['mbl']
		data.email=request.POST['email']
		data.address=request.POST['addr']
		data.save()
		# return HttpResponse("Updated")
		return redirect('/read')

	return render(request,'CrudApp/update.html',{'info':data})

def delete(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.delete()
		return redirect('/read')
	return render(request,'CrudApp/delete.html',{'data':data})


def reg(request):
	if request.method=="POST":
		f=StudentForm(request.POST)
		f.save()
		return HttpResponse("submited")
	f=StudentForm()
	return render(request,'CrudApp/reg.html',{'form':f})


def fetch(request):
	data=Student.objects.all()
	return render(request,'CrudApp/fetch.html',{'data':data})


def edit(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/fetch')
	form=StudentForm(instance=data)
	return render(request,'CrudApp/edit.html',{'form':form})


def de(request,id):
	ob=Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/fetch')
	return render(request,'CrudApp/de.html',{'info':ob})


def email(request):
	if request.method=="POST":
		email=request.POST['email']
		subject=request.POST['subject']
		body=request.POST['body']
		sender=settings.EMAIL_HOST_USER
		reciver=email
		send_mail(subject,body,sender,[reciver])
		return HttpResponse("<h2>Please check your mail</h2>"+email)

	return render(request,'CrudApp/email.html')