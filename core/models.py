from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

 
'''
creating the supplier object and slugifying it, 
for use in resolving supplier details
'''

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=65, blank=False)
    supplier_email = models.EmailField(max_length=100, blank=False)
    supplier_phone = models.IntegerField()
    supplier_slug = models.SlugField(editable=False, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.supplier_name
    
    def get_absolute_url(self):
        self.supplier_slug = slugify(self.supplier_name)
        return f'/{self.supplier_slug}/'

'''
creating the item object 
'''
class Item(models.Model):
    name = models.CharField(max_length=65, blank=False)
    desc = models.TextField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateField(auto_now_add=True, blank=False, null=True, editable=False)
    quantity = models.IntegerField()
    supplier = models.ManyToManyField(Supplier, related_name='items')
    item_slug = models.SlugField(editable=False, blank=True, null=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        self.item_slug = slugify(self.name)
        return f'/{self.item_slug}/'
    
    
       
