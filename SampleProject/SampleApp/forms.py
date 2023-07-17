from django import forms
from .models import  Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='__all__'

		widgets={
			"name":forms.TextInput(attrs={"placeholder":"Enter Name",'class':'Name','class':'form-control'}),
			"rollnum":forms.TextInput(attrs={"placeholder":"Enter Rollnumber",'class':'rollnum','class':'form-control'}),
			"age":forms.NumberInput(attrs={"required":False,"placeholder":"Enter Age",'class':'age','class':'form-control'},),
			"mobile":forms.NumberInput(attrs={"placeholder":"Enter mobile number",'class':'mobile','class':'form-control'}),
			"email":forms.EmailInput(attrs={'placeholder':'Enter Email','class':'email','class':'form-control'}),
			"address":forms.TextInput(attrs={"placeholder":"Enter Name",'class':'address','class':'form-control'})
			
			

			
		}