from rest_framework import serializers
from .models import Item, Supplier

class ItemSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(many=True, slug_field='supplier_name', queryset=Supplier.objects.all())
    
    class Meta:
        model = Item
        fields = ['id', 'name', 'desc', 'price', 'quantity', 'supplier', 'date_added', 'get_absolute_url']
    
    
    
class SupplierSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(many=True, queryset=Item.objects.all(), slug_field='name')
    
    class Meta:
        model = Supplier
        fields = ['id', 'supplier_name', 'supplier_email', 'supplier_phone', 'get_absolute_url', 'items']
        
        