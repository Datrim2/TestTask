from django.db import models
from django.contrib.auth.models import User

class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=1000, verbose_name="")
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.doc_name

class Product(models.Model):
    files = models.ForeignKey(Files, on_delete=models.CASCADE)
    client = models.IntegerField()
    tps = models.DecimalField(max_digits=50,decimal_places=25)
    latency = models.DecimalField(max_digits=50,decimal_places=25)
    stddev = models.DecimalField(max_digits=50,decimal_places=25)