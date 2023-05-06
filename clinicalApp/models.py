from django.db import models

# Create your models here.
class patients(models.Model):
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    age = models.IntegerField()

class clinicalData(models.Model):
    COMPONENTS_NAME =[('hw','Height/Weight'),('bp','Blood Presure'),('heartrate','Heart Rate')]
    componentName = models.CharField(choices=COMPONENTS_NAME, max_length=20)
    componetValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField(auto_now_add='True')
    patient = models.ForeignKey(patients,on_delete=models.CASCADE) # One to Many Relationship between both class or tables
