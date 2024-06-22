from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class User(AbstractUser):
    phone_number = models.CharField("電話番号", max_length=32)
    
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "ユーザー"
        db_table = "user"
