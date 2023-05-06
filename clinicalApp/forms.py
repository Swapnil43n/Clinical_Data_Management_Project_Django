from django import forms
from clinicalApp.models import clinicalData, patients

class patientForm(forms.ModelForm):
    class Meta:
        model = patients
        fields = '__all__'
class clinicalDataForm(forms.ModelForm):
    class Meta:
        model = clinicalData
        fields ='__all__'
