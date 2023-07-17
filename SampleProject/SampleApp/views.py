from django.shortcuts import render,redirect
from SampleApp.forms import StudentForm
from SampleApp.models import Student
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def temp(request):
	return render(request,'SampleApp/temp.html')

def dynamic(request,id,name):
	return render(request,'SampleApp/dyn.html',{'i':id,'n':name})

def inline(request):
	return render(request,'SampleApp/inline.html')

def internal(request):
	return render(request,'SampleApp/internal.html')

def external(request):
	return render(request,'SampleApp/external.html')

def boot(request):
	return render(request,'SampleApp/boot.html')

def offline(request):
	return render(request,'SampleApp/offline.html')

def reg(request):
	if request.method=="POST":
		f=StudentForm(request.POST)
		f.save()
		return HttpResponse("done")
	f=StudentForm()
	return render(request,'SampleApp/reg.html',{'form':f})

def read(request):
	data=Student.objects.all()
	return render(request,'SampleApp/read.html',{'data':data})

def edit(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/read')
	form=StudentForm(instance=data)
	return render(request,'SampleApp/edit.html',{'form':form,'data':data})




def email(request):
	if request.method=='POST':
		email=request.POST['email']
		subject=request.POST['subject']
		body=request.POST['body']
		sender=settings.EMAIL_HOST_USER
		reciver=email
		send_mail(subject,body,sender,[reciver])
		return HttpResponse("<h2>Please check This Mail</h2> "+email)
	return render(request,'SampleApp/email.html')
