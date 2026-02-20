from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mechanic(models.Model):
    full_name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    services = models.ManyToManyField(
        'Service',
        blank=True,
        related_name='mechanics_m2m'
    )

    def __str__(self):
        return self.full_name


class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    mechanic = models.ForeignKey(
        Mechanic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='services_fk'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name