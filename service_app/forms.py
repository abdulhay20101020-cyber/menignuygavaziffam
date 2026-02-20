from django import forms
from .models import ServiceCategory, Mechanic, Service

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['name']

class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['full_name', 'experience', 'phone', 'is_active', 'services']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'category', 'price', 'description', 'is_available', 'mechanic']