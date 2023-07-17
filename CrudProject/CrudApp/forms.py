from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='__all__'

		widgets={
			"name":forms.TextInput(attrs={"placeholder":"Enter your name",'class':'name','class':'form-control'}),
			"rollnum":forms.TextInput(attrs={"placeholder":"Enter your rollnumber",'class':'rollnumber','class':'form-control'}),
			"age":forms.NumberInput(attrs={"placeholder":"Enter your age",'class':'age','class':'form-control'}),
			"mobile":forms.NumberInput(attrs={"placeholder":"Enter your mobile number",'class':'mobile','class':'form-control'}),
			"email":forms.EmailInput(attrs={"placeholder":"Enter your email",'class':'email','class':'form-control'}),
			"address":forms.TextInput(attrs={"placeholder":"Enter your address",'class':'address','class':'form-control'})
		}