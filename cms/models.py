from django.db import models
from datetime import datetime,date

# Create your models here.
class provider(models.Model):
    name = models.TextField(null=True)

    def __str__(self):
        return self.name

class Credit(models.Model):
    bill_date = models.DateField(default=date.today)
    amount = models.IntegerField()
    provider = models.ForeignKey(provider, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    

    

