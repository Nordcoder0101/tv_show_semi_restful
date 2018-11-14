from django.db import models

class ShowManager(models.Manager):
    def basic_validation(self, postData):
        errors = {}

        if len(postData['title']) == 0:
            errors['title'] = "Please provide a name for your show"
        if len(postData['network']) < 2:
            errors['network'] = "Please provide a valid network"
        if not postData['release_date']:
            errors['release_date'] = "Please provide a release date"
        if len(postData['description']) < 5:
            errors['description'] = "Please provide a description at least 5 characters long"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.CharField(max_length=500, null=True)
    objects = ShowManager()

