from django.shortcuts import render
from .forms import *
# Create your views here.

def home(request):
    emrForm = EMRForm(request.POST)
    data = EMR.objects.all()
    if(emrForm.is_valid()):
        emrForm.save()
        return(render(request, "index.html", {'form' : emrForm, 'data' : data}))
    
    return(render(request, "index.html", {'form' : emrForm,  'data' : data}))