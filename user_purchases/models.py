from django.db import models
from user_accounts.models import UserModel
from cake_items.models import CakeModel
# Create your models here.

CAKE_SIZE = (
    ('1', 'Small (1kg)'),
    ('2', 'Medium (1.5kg)'),
    ('3', 'Large (2kg)'),
)

CAKE_SIZE_PRICES = {
    '1': 1.0, 
    '2': 1.5, 
    '3': 2.0,  
}

DELIVERY_STATUS = (
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)

class UserPurchase(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    cake = models.ForeignKey(CakeModel, on_delete=models.CASCADE)
    cake_size = models.CharField(max_length=100, choices=CAKE_SIZE)
    total_price = models.IntegerField()
    status = models.CharField(choices=DELIVERY_STATUS, max_length=100, default='processing')

    def save(self, *args, **kwargs):
        size = CAKE_SIZE_PRICES.get(self.cake_size, 1)
        self.total_price = self.cake.price *size
        super(UserPurchase, self).save(*args, **kwargs)



