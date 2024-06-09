from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import UserReview
from .serializers import UserReviewSerializer
from category.permissions import IsAdminUserRole
from user_purchases.models import UserPurchase
# Create your views here.


class UserReviewListView(generics.ListAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [IsAdminUserRole, IsAuthenticated]


class UserReviewDetailView(generics.RetrieveAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [IsAuthenticated]

class UserReviewCreateView(generics.CreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        cake = serializer.validated_data['cake']

        if not UserPurchase.objects.filter(user=user, cake=cake ).exists():
            raise PermissionDenied('You can only comment on a cake you have purchased!')
        serializer.save(user=user)
        

class UserReviewUpdateView(generics.UpdateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionDenied('You do not have permission to update this comment!')
        serializer.save()


class UserReviewDeleteView(generics.DestroyAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.user:
            raise PermissionDenied('You can not delete this comment')

        instance.delete()