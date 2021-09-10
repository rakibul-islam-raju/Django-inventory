from django.shortcuts import get_object_or_404
from rest_framework import generics, response
from rest_framework import permissions
from rest_framework.views import APIView

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


class CustomerSingleObject(APIView):
    '''
        single object
    '''

    def get(self, request, *args, **kwargs):
        phone = request.GET.get('phone')
        customer = get_object_or_404(Customer, phone=phone)
        return response.Response({'customer': CustomerSerializer(instance=customer).data})


class SellProductListCreate(generics.ListCreateAPIView):
    '''
        create view
    '''
    model = SellProductItem
    serializer_class = SellProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class SellProductDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
        detail view
    '''
    serializer_class = SellProductEditSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = SellProductItem.objects.all()

    def perform_update(self, serializer):
        serializer.save(added_by=self.request.user)
