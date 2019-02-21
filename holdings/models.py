from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Holdingmutual(models.Model):
    no_shares=models.IntegerField(default=None)#amfi code for product
    #rating=models.IntegerField(default=1)#rating of stock
    #image=models.ImageField(upload_to='images/')
    #icon=models.ImageField(upload_to='images/',null=True)
    start_date=models.DateField(default=None)
    sip_date=models.DateField(default=None,null=True)
    notes=models.TextField(default=None,blank=True)#Notes
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