from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('list/', views.CategoryListView.as_view(), name='category_list'),
    path('list/<int:pk>', views.CategoryDetailsView.as_view(), name='category_detail'),
    path('create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('update/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),
]
