from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ItemSerializer, SupplierSerializer
from .models import Item, Supplier
from rest_framework import status
from django.http import Http404
from rest_framework.generics import GenericAPIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

# list of items in stock
class AllItems(GenericAPIView):
    serializer_class = ItemSerializer
    @swagger_auto_schema(
        operation_description="view a list of all items in the database",
        responses={200:ItemSerializer}
    )
    
    def get(self, request, format=None):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


# list of suppliers
class AllSuppliers(GenericAPIView):
    serializer_class = SupplierSerializer
    @swagger_auto_schema(
        operation_description="View a list of all Suppliers recorded",
        responses={200:SupplierSerializer}
    )
    
    def get(self, request, format=None):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# new item

class AddToInventory(APIView):
    serializer_class = ItemSerializer
    
    @swagger_auto_schema(
        operation_description="Create a new item",
        request_body=ItemSerializer,  
        responses={
            201: ItemSerializer,  
            400: 'Bad Request - Invalid data'
        }
    )
    
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

# adding Suppliers
class AddSupplier(APIView):
    serializer_class = SupplierSerializer
    
    @swagger_auto_schema(
        operation_description="Add a Supplier to the records",
        request_body=SupplierSerializer,  
        responses={
            201: SupplierSerializer,
            400: 'Bad Request - Invalid data'
        }
    )
    
    def post(self, request, format=None):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
# creating detail views for both item and supplier

# item detail

class ItemDetail(APIView):
    serializer_class = ItemSerializer
    
    def get_object(self, item_slug):
        try:
            return Item.objects.get(item_slug=item_slug)
        except Item.DoesNotExist:
            raise Http404
        
    @swagger_auto_schema(
        operation_description="Retrieve an item in the inventory by its slug",
        responses={200: SupplierSerializer(many=False), 404: 'Not Found'},
        manual_parameters=[openapi.Parameter(
            'item_slug',
            openapi.IN_PATH,
            description="Slug of the item to retrieve",
            type=openapi.TYPE_STRING
        )]
    )
    
    def get(self, request, item_slug, format=None):
        item = self.get_object(item_slug)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status.HTTP_200_OK)
      
    @swagger_auto_schema(
        operation_description="Update an item in the inventory by its slug",
        request_body=ItemSerializer,
        responses={202: ItemSerializer, 400: 'Invalid data'},
    )
    
    def put(self, request, item_slug, format=None):
        item = self.get_object(item_slug)
        serializer = ItemSerializer(item, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(
        operation_description="Delete an item by its slug",
        responses={
            204: 'No Content - Successfully deleted',
            404: 'Not Found - Item does not exist'
        }
    )
    
    def delete(self, request, item_slug, format=None):
        item = self.get_object(item_slug)
        item.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    
class SupplierInfo(GenericAPIView):
    serializer_class = SupplierSerializer 
    def get_object(self, supplier_slug):
        try:
            return Supplier.objects.get(supplier_slug=supplier_slug)
        except Supplier.DoesNotExist:
            raise Http404
         
         
    @swagger_auto_schema(
        operation_description="Retrieve a supplier's information by its slug",
        responses={200: SupplierSerializer(many=False), 404: 'Not Found'},
        manual_parameters=[openapi.Parameter(
            'supplier_slug',
            openapi.IN_PATH,
            description="Slug of the supplier to retrieve",
            type=openapi.TYPE_STRING
        )]
    )
    
    def get(self, request, supplier_slug, format=None):
        supplier = self.get_object(supplier_slug)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data, status.HTTP_200_OK)
       
    @swagger_auto_schema(
        operation_description="Update a supplier's information by its slug",
        request_body=SupplierSerializer,
        responses={202: SupplierSerializer, 400: 'Invalid data'},
    )
    
    def put(self, request, supplier_slug, format=None):
        supplier = self.get_object(supplier_slug)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    