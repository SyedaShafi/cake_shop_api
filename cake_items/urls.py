from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CakeListView.as_view(), name='cake_list'),
    path('create/', views.CakeCreateView.as_view(), name='cake_create'),
    path('list/<int:pk>', views.CakeDetailView.as_view(), name='cake_detail'),
    path('update/<int:pk>', views.CakeUpdateView.as_view(), name='cake_update'),
    path('delete/<int:pk>', views.CakeDeleteView.as_view(), name='cake_delete'),
]
