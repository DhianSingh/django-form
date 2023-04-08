

# Create your views here.
from django.shortcuts import render  
from polls.forms import StudentForm  
  
def index(request):  
    student = StudentForm()  
    return render(request,"index.html",{'form':student})  