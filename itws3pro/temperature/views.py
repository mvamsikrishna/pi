from __future__ import unicode_literals
from .models import Temperature 
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
	temp_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	temp_data=str(temp_data)	
	context={'tem':temp_data}
	return render(request,'temperature/index.html',context)
def getdata(request):
	if request.method=='GET' :
		temp_value=request.GET['temperature']
		t_obj=Temperature()
		t_obj.tem_value=temp_value
		t_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")
