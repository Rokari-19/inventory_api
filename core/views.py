from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ItemSerializer, SupplierSerializer
from .models import Item, Supplier
from rest_framework import status
from django.http import Http404
# Create your views here.

# list of items in stock
class AllItems(APIView):
    def get(self, request, format=None):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


# list of suppliers
class AllSuppliers(APIView):
    def get(self, request, format=None):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# new item

class AddToInventory(APIView):
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

# adding Suppliers
class AddSupplier(APIView):
    def post(self, request, format=None):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
# creating detail views for both item and supplier

# item detail

class ItemDetail(APIView):
    def get_object(self, item_slug):
        try:
            Item.objects.get(item_slug=item_slug)
        except Item.DoesNotExist:
            raise Http404
        
    def get(self, request, item_slug, format=None):
        item = self.get_object(item_slug)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, item_slug, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        