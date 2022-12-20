import django.forms as forms
from . models import *

class EMRForm(forms.ModelForm):

    class Meta:
        model = EMR
        fields = "__all__"