from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserPurchase
from rest_framework.exceptions import PermissionDenied
from .serializers import UserPurchaseSerializer, UserPurchaseSerializerWithAllFields
from category.permissions import IsAdminUserRole
# Create your views here.

class UserPurchaseList(generics.ListAPIView):
    queryset = UserPurchase.objects.all()
    serializer_class = UserPurchaseSerializerWithAllFields
    permission_classes = [IsAuthenticated]


class UserPurchaseDetailView(generics.RetrieveAPIView):
    queryset = UserPurchase.objects.all()
    serializer_class = UserPurchaseSerializerWithAllFields
    permission_classes = [IsAuthenticated]


class UserPurchaseCreateView(generics.CreateAPIView):
    queryset = UserPurchase.objects.all()
    serializer_class = UserPurchaseSerializer
    # permission_classes = [IsAuthenticated]

class UserPurchaseUpdateView(generics.CreateAPIView):
    queryset = UserPurchase.objects.all()
    serializer_class = UserPurchaseSerializerWithAllFields
    permission_classes = [IsAuthenticated, IsAdminUserRole]


class UserPurchaseDeleteView(generics.DestroyAPIView):
    queryset = UserPurchase.objects.all()
    serializer_class = UserPurchaseSerializer
    permission_classes = [IsAuthenticated]


    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied('You do not have permissions to delete this data')
    
        if instance.status != 'delivered' :
            raise PermissionDenied('You can Only Delete the Purchase data that are Deliverd!')

        instance.delete()





