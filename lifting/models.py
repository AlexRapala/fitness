from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Log(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class Lift(models.Model):
    name = models.CharField(max_length=1024)

class LogXLift(models.Model):
    log = models.ForeignKey(Log, on_delete=models.PROTECT)
    lift = models.ForeignKey(Lift, on_delete=models.PROTECT)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    lifted_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)