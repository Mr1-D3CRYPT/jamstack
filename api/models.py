from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    uid = models.AutoField(primary_key=True)
    reg = models.ForeignKey(User, on_delete=models.CASCADE)
    compt = models.CharField(max_length=300)
    status = models.CharField(max_length=10, default="registered")

    def __str__(self):
        return f"{self.uid} - {self.reg}"