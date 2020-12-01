from django import forms
from .models import *

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = '__all__'


class FashionForm(forms.ModelForm):
    class Meta:
        model = Fashion
        fields = '__all__'
        

class GadgetsForm(forms.ModelForm):
    class Meta:
        model = Gadgets
        fields = '__all__'
