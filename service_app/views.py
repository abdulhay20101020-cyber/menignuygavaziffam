from django.shortcuts import render, redirect
from .models import ServiceCategory, Mechanic, Service
from .forms import ServiceCategoryForm, MechanicForm, ServiceForm

# --- Categories ---
def category_list(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'service_app/category_list.html', {'categories': categories})

def add_service_category(request):
    form = ServiceCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'service_app/add_service_category.html', {'form': form})

# --- Mechanics ---
def mechanic_list(request):
    mechanics = Mechanic.objects.all()
    return render(request, 'service_app/mechanic_list.html', {'mechanics': mechanics})

def add_mechanic(request):
    form = MechanicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mechanic_list')
    return render(request, 'service_app/add_mechanic.html', {'form': form})

# --- Services ---
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_app/service_list.html', {'services': services})

def add_service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    return render(request, 'service_app/add_service.html', {'form': form})