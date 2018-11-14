from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.CharField(max_length=500, null=True)
    

