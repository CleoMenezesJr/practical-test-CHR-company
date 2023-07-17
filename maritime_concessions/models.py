from django.db import models


# Create your models here.
class Concession(models.Model):
    number = models.CharField(max_length=10)
    concession_number = models.CharField(max_length=10)
    concession_type = models.CharField(max_length=200)
    commune = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rs_ds = models.CharField(max_length=20)
    tramite_type = models.CharField(max_length=200)
    concessionaire = models.CharField(max_length=200)
    vigency_type = models.CharField(max_length=200)

    def __str__(self):
        return f"Concession {self.number} - {self.concession_type}"
