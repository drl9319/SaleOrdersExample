from django.db import models
from django.utils import timezone
from django.core.mail import send_mail


class Product(models.Model):
    SerialNumber = models.CharField(max_length=60)
    Name = models.CharField(max_length=200)
    Description= models.CharField(max_length=1000)
    Price= models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.Name

class Client(models.Model):
    COUNTRIES = (
        ('SP', 'Spain'),
        ('GR', 'Germany'),
        ('PR', 'Portugal'),
        ('IT', 'Italy'),
    )

    Name = models.CharField(max_length=200)
    Nif = models.CharField(max_length=50)
    Country = models.CharField(max_length=2, choices=COUNTRIES)
    City = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class SaleOrder(models.Model):
    Date = models.DateField(default=timezone.now)
    IdClient = models.ForeignKey(Client, on_delete=models.CASCADE)

    '''
    def __str__(self):
        return self.Date
    '''

    def save(self, *args, **kwargs):
        send_mail(
            'You are new Client order to manage',
            'Here is the message.',
            'drodriguezahora@gmail.com',
            ['drl.9319@gmail.com'],
            fail_silently=False,
        )
        super(SaleOrder, self).save(self, *args, **kwargs)


class SaleOrderLine(models.Model):
    IdSale = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    IdProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    Price= models.DecimalField(max_digits=12, decimal_places=2)
    Qty = models.IntegerField(default=0)

    '''
    def __str__(self):
        return self.IdProduct
    '''
