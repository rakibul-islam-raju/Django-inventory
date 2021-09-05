from rest_framework import generics
from rest_framework import permissions

from sell.models import *
from sell.api.serializers import *


class CustomerListCreate(generics.ListCreateAPIView):
    '''
        create view
    '''
    model = Customer
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.filter(status=True)


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
        detail view
    '''
    model = Customer
    serializer_class = CustomerEditSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.filter(status=True)


class SellProductListCreate(generics.ListCreateAPIView):
    '''
        create view
    '''
    model = SellProduct
    serializer_class = SellProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = SellProduct.objects.all()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class SellProductDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
        detail view
    '''
    model = SellProduct
    serializer_class = SellProductEditSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = SellProduct.objects.all()

    def perform_update(self, serializer):
        serializer.save(added_by=self.request.user)
