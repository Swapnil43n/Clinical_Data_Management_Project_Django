from django.shortcuts import render , redirect
from clinicalApp.models import patients , clinicalData
from django.views.generic import ListView,CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from clinicalApp.forms import clinicalDataForm 

# Create your views here.
class patientsListView(ListView):
    model = patients

class patientsCreateView(CreateView):
    model = patients
    success_url = reverse_lazy('index')
    fields = ('firstName','lastName','age')

class patientsUpdateView(UpdateView):
    model = patients
    success_url = reverse_lazy('index')
    fields = ('firstName','lastName','age')

class patientsDeleteView(DeleteView):
    model = patients
    success_url = reverse_lazy('index')
   
def addData(request,**kwargs):
    form = clinicalDataForm()
    patient = patients.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = clinicalDataForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    return render(request,'clinicalApp/clinicaldata_form.html',{'form':form, 'patient':patient})

def analyze(request,**kwargs):
    data = clinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData =[]
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightAndweight = eachEntry.componetValue.split('/')
            if len(heightAndweight) >1:
                feetToMeter = float(heightAndweight[0])* 0.4536
                BMI =(float(heightAndweight[1])) / ( feetToMeter * feetToMeter)
                bmiEntry = clinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componetValue = BMI
                responseData.append(bmiEntry)
            responseData.append(eachEntry)
    return render(request,'clinicalApp/generatereport.html',{'data':responseData})

                  
