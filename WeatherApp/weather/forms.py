from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control form-control-dark w-100', 'name':'city','id':'city',
                                            'aria-label':'Search', 'placeholder':'Input your city','type':'text'})}


