from django.db import models

# Create your models here.
class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=25)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.ethnicity