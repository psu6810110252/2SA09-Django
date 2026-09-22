from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import secrets

class AuthToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=64, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def for_user(cls, user):
        token, _ = cls.objects.get_or_create(
            user=user,
            defaults={"key": secrets.token_hex(32)}
        )
        return token

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username