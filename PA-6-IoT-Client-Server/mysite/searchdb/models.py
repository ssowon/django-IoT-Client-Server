from django.db import models


# Create your models here.
class Sensorvalue(models.Model):
    no = models.CharField(max_length=10)
    datein = models.DateTimeField(auto_now=False, auto_now_add=False)
    cds = models.IntegerField(default=0)
    led = models.IntegerField(default=0)

    def __str__(self):
        return self.no
