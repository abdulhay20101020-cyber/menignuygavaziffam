from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory, Mechanic, Service


def home(request):
    return render(request, 'service_app/home.html', {
        'categories': ServiceCategory.objects.all(),
        'mechanics': Mechanic.objects.all(),
        'services': Service.objects.all()
    })


def services_by_category(request, name):
    services = Service.objects.filter(category__title=name, is_available=True)
    return render(request, 'service_app/category.html', {
        'services': services,
        'category': name
    })


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    other = Service.objects.filter(mechanic=service.mechanic).exclude(id=id)
    return render(request, 'service_app/detail.html', {
        'service': service,
        'other': other
    })


def services_by_mechanic(request, id):
    mechanic = get_object_or_404(Mechanic, id=id)
    services = Service.objects.filter(mechanic=mechanic)
    return render(request, 'service_app/mechanic.html', {
        'mechanic': mechanic,
        'services': services,
        'experienced': mechanic.experience_year >= 3
    })
