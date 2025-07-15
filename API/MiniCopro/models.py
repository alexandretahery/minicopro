from django.db import models

# Create your models here.
class Annonce(models.Model):
    id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    condominium_expenses = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title