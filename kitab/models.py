from django.db import models


class kitablar(models.Model):
    bookname = models.CharField(max_length=100)
    desc = models.TextField()
    pages = models.IntegerField() 


    








# Create your models here.
