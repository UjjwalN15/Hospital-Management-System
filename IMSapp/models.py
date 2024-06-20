from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import Patient
#For total
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
# Create your models here.    
class ProductCategory(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name #returns the name in admin panel
    
    
class Department(models.Model):
    name = models.CharField(max_length = 200)
    floor = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    stock = models.IntegerField()
    category = models.ForeignKey(ProductCategory,on_delete = models.SET_NULL, null = True)
    price = models.IntegerField(null=True)
    department = models.ManyToManyField(Department)
    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    
class Purchase(models.Model):
    patient = models.ForeignKey(Patient, related_name='purchase', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    price = models.FloatField(null=True)
    # product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)  CASCADE removes all the data when the Department is deleted
    product = models.ForeignKey(Product,on_delete = models.CASCADE) #models.SET_NULL replaces the NUll value if Product is deleted
    supplier = models.ForeignKey(Supplier,on_delete = models.SET_NULL, null = True) 
    
class Billing(models.Model):
    patient = models.ForeignKey(Patient, related_name='billing', on_delete=models.CASCADE,null=False,blank=False)
    purchase = models.ManyToManyField(Purchase)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=100, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')])
    
@receiver(m2m_changed, sender=Billing.purchase.through)
def update_billing_total(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.total = sum(purchase.price * purchase.quantity for purchase in instance.purchase.all())
        instance.save()

    

