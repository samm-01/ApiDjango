from django.db import models

# Create your models here.

class employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField()
    esal = models.FloatField()


    def __str__(self):
        return f"{self.eid}--{self.ename}"