from django import forms 
from formAPP.models import Proyecto

class formProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'