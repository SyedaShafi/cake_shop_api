from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from category.permissions import IsAdminUserRole
from . models import CakeModel
from . serializers import CakeSerializer
# Create your views here.


class CakeListView(generics.ListAPIView):
    queryset = CakeModel.objects.all()
    serializer_class = CakeSerializer


class CakeCreateView(generics.CreateAPIView):
    queryset = CakeModel.objects.all()
    serializer_class = CakeSerializer
    permission_classes = [IsAdminUserRole, IsAuthenticated]



class CakeDetailView(generics.RetrieveAPIView):
    queryset = CakeModel.objects.all()
    serializer_class = CakeSerializer


class CakeUpdateView(generics.UpdateAPIView):
    queryset = CakeModel.objects.all()
    serializer_class = CakeSerializer
    permission_classes = [IsAdminUserRole, IsAuthenticated]

class CakeDeleteView(generics.DestroyAPIView):
    queryset = CakeModel.objects.all()
    serializer_class = CakeSerializer
    permission_classes = [IsAdminUserRole, IsAuthenticated]





