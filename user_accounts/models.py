from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
USER_ROLE= (
    ('user', 'user'),
    ('admin', 'admin'),
)
class UserModel(AbstractUser): 
    role = models.CharField(max_length=40, default='user', choices=USER_ROLE)
    def __str__(self):
        return self.username
    