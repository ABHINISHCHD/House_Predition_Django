from pyexpat import model
from django.db import models

# Create your models here.
class predresult(models.Model):
    salary=models.FloatField()
    age=models.FloatField()
    room=models.FloatField()
    bedroom=models.IntegerField()
    population=models.IntegerField()
    price=models.FloatField()