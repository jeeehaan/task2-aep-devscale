from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)