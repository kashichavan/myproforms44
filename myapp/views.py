from django.shortcuts import render
from .models import StudentModel
from .forms import StudentForm,StudentForm2


# Create your views here.
def studentview(request):
    if request.method=='POST':
            form=StudentForm(request.POST)
            if form.is_valid():
                  name=form.cleaned_data['name']
                  age=form.cleaned_data['age']
                  StudentModel.objects.create(name=name,age=age)
    f=StudentForm()
    return render(request,'student.html',context={'form':f})





def studentview2(request):
    if request.method=='POST':
        form=StudentForm2(request.POST) 
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            StudentModel.objects.create(name=name,age=age)
        else:
             raise ValueError("Form is invalid")
    f=StudentForm2()
    return render(request,'student.html',context={'form':f})
