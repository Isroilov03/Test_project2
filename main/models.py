from django.db import models

# Create your models here.


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.IntegerField()
    t_yil = models.DateField()
    created = models.TimeField()



