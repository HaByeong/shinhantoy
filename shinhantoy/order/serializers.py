from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.Modelserializer):
  class Meta:
    model=Order
    filter='__all__'
