from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel


class Bank(BaseModel):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
