from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Books(models.Model):
    book_id = models.CharField(max_length=12,primary_key=True)
    name    = models.CharField(max_length=100)
    count   = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        

class Subscribers(models.Model):
    subscriber_id = models.CharField(max_length=15)
    book_id       = models.CharField(max_length=12)
    name          = models.CharField(max_length=20)
    date          = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))

    class Meta:
        unique_together = (("subscriber_id", "book_id"))
    
    def __str__(self):
        return self.subscriber_id,self.book_id,self.name
