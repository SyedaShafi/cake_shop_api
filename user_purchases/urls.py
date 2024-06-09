from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.UserPurchaseList.as_view(), name='purchase_list'),

    path('list/<int:pk>', views.UserPurchaseDetailView.as_view(), name='purchase_list'),

    path('create/', views.UserPurchaseCreateView.as_view(), name='purchase_create'),

    path('update/<int:pk>', views.UserPurchaseUpdateView.as_view(), name='purchase_create'),

    path('delete/<int:pk>', views.UserPurchaseDeleteView.as_view(), name='purchase_delete'),
]


