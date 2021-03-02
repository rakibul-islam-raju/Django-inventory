from rest_framework import serializers
from core.models import *

# Create serializer
class WarehouseSerializer(serializers.ModelSerializer):
    '''
        create serializer
    '''
    class Meta:
        model = Warehouse
        exclude = ['status', 'date_added']


class WarehouseEditSerializer(serializers.ModelSerializer):
    '''
        Edit serializer
    '''
    class Meta:
        model = Warehouse
        exclude = ['date_added']


class CategorySerializer(serializers.ModelSerializer):
    '''
        create serializer
    '''
    class Meta:
        model = Category
        exclude = ['status', 'date_added']


class CategoryEditSerializer(serializers.ModelSerializer):
    '''
        Edit serializer
    '''
    class Meta:
        model = Category
        exclude = ['date_added']


class SubcategorySerializer(serializers.ModelSerializer):
    '''
        Create serializer
    '''
    class Meta:
        model = Subcategory
        exclude = ['status', 'date_added']


class SubcategoryEditSerializer(serializers.ModelSerializer):
    '''
        edit serializer
    '''
    class Meta:
        model = Subcategory
        exclude = ['date_added']


class ProductSerializer(serializers.ModelSerializer):
    '''
        Create serializer
    '''
    class Meta:
        model = Product
        exclude = ['status', 'date_added', 'date_updated']


class ProductEditSerializer(serializers.ModelSerializer):
    '''
        edit serializer
    '''
    class Meta:
        model = Product
        exclude = ['date_added', 'date_updated']


class BankSerializer(serializers.ModelSerializer):
    '''
        Create serializer
    '''
    class Meta:
        model = Bank
        exclude = ['status', 'date_added']


class BankEditSerializer(serializers.ModelSerializer):
    '''
        edit serializer
    '''
    class Meta:
        model = Bank
        exclude = ['date_added']


class BankTransactionSerializer(serializers.ModelSerializer):
    '''
        Create serializer
    '''
    class Meta:
        model = BankSerializer
        exclude = ['status', 'date_added', 'date_updated']


class BankTransactionEditSerializer(serializers.ModelSerializer):
    '''
        edit serializer
    '''
    class Meta:
        model = BankSerializer
        exclude = ['date_added', 'date_updated']

