from rest_framework import serializers
from .models import Restaurant, MenuItem, Order

# Restaurant Serializer
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number']

# MenuItem Serializer
class MenuItemSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'name', 'description', 'price']

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_address', 'menu_items', 'total_price', 'status', 'created_at']
