# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_head = models.BooleanField(default=False)
    is_dos = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_lab = models.BooleanField(default=False)