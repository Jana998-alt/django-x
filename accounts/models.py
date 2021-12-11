from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # when customizing the user, do not do the migrations first, you have to define the custom user first.
    # you can edit bet there is a process ...
    phone_number  = models.CharField(max_length=15, null = True, blank= True)

    def __str__(self):
        return self.email