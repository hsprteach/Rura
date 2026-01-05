from django.db import models

# Create your models here.
class Learner(models.Model):
    lastName = models.CharField(max_length=50)
    firstNames = models.CharField(max_length=50)
    grade = models.IntegerField(default=8)
    group = models.CharField(max_length=1)
    status = models.IntegerField(default=0)



