from django.urls import path, include
from .views import AllItems, AllSuppliers, AddSupplier, AddToInventory, ItemDetail

urlpatterns = [
    path('all-items/', AllItems.as_view()),
    path('all-suppliers/', AllSuppliers.as_view()),
    path('add-to-inventory/', AddToInventory.as_view()),
    path('add-supplier/', AddSupplier.as_view()),
    path('items/<slug:item_slug>/', ItemDetail.as_view()),
]