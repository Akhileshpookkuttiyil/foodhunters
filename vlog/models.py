from django.db import models
import django
from datetime import datetime
# Create your models here.
class Vlog(models.Model):
    title=models.CharField(max_length=250,db_index=True)
    c = django.utils.timezone.now
    date = models.DateField(default=c)
    location=models.CharField(max_length=150)
    image=models.ImageField(upload_to='pics/',default='default.jpg')
    description=models.TextField()
    author=models.CharField(max_length=30, default='unknown')

    def __str__(self):
        return self.title

    
    
    
