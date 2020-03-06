from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Holdingmutual(models.Model):
    no_shares=models.IntegerField(default=None)#amfi code for product
    #rating=models.IntegerField(default=1)#rating of stock
    #image=models.ImageField(upload_to='images/')
    #icon=models.ImageField(upload_to='images/',null=True)
    start_date=models.DateField(default=None)
    sip_date=models.DateField(default=None,null=True)
    notes=models.TextField(default=None,blank=True)#Notes
    investment_type=models.CharField(max_length=10,default='unknown',blank=True)#Investment type buy or sip
    productid=models.ForeignKey('products.Product',on_delete=models.CASCADE)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)

 
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d %a %Y")
    
    def __str__(self):
        return '%s' % self.productid

    def get_absolute_url(self):
        return reverse('portfolio')

class Holdingmutualsip(models.Model):
    
    #rating=models.IntegerField(default=1)#rating of stock
    #image=models.ImageField(upload_to='images/')
    #icon=models.ImageField(upload_to='images/',null=True)
    def return_date_time():
        now = timezone.now()
        return now + timedelta(days=1000)
    
    date=models.DateField(default=None)
    end_date=models.DateField(default=return_date_time)    
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    invest_amount=models.IntegerField(default=None)#amfi code for product 
    productid=models.ForeignKey('products.Product',on_delete=models.CASCADE)  
    
      
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d %a %Y")
    
    def __str__(self):
        return '%s' % self.productid

    def get_absolute_url(self):
        return reverse('portfolio')