from django.db import models
from cake_items.models import CakeModel
from user_accounts.models import UserModel
# Create your models here.
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class UserReview(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    cake = models.ForeignKey(CakeModel, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.CharField(max_length=100, choices=STAR_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)




