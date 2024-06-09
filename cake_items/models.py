from django.db import models
from user_accounts.models import UserModel
from category.models import Category
# Create your models here.
DELIVERY = (
    ('1', 'Same Day Delivery'),
    ('2', 'Next Day Delivery')
)


class CakeModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Category, on_delete=models.CASCADE)
    delivery_type = models.CharField(choices = DELIVERY, max_length=100)
    cake_description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cake_items/images/')

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return None
    
 