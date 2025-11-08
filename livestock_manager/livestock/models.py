
from django.db import models
from django.contrib.auth.models import User

class Livestock(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    health_status = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.animal_name
