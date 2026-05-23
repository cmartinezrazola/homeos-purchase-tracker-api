from django.shortcuts import render
from rest_framework import viewsets
from .models import Marketplace, OrderItem, Order
from .serializers import (
    MarketplaceSerializer,
    OrderItemSerializer, 
    OrderSerializer,
)

class MarketplaceViewSet(viewsets.ModelViewSet):
    queryset = Marketplace.objects.all()
    serializer_class = MarketplaceSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
