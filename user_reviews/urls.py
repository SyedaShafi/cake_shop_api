from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.UserReviewListView.as_view(), name='review_list'),
    path('list/<int:pk>', views.UserReviewDetailView.as_view(), name='review_detail'),
    path('create/', views.UserReviewCreateView.as_view(), name='review_create'),
    path('update/<int:pk>', views.UserReviewUpdateView.as_view(), name='review_update'),
    path('delete/<int:pk>', views.UserReviewDeleteView.as_view(), name='review_delete'),
]
