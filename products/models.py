from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    stockid=models.IntegerField(default=None)#amfi code for product
    title=models.CharField(max_length=200)#Title of mutual fund
    #rating=models.IntegerField(default=1)#rating of stock
    body=models.TextField()#Description of product
    #image=models.ImageField(upload_to='images/')
    #icon=models.ImageField(upload_to='images/',null=True)
    #from_date=models.DateTimeField(default=None)
    #to_date=models.DateTimeField(default=None)
    #hunter=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d %a %Y")
