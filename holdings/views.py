from django.shortcuts import render,get_object_or_404
from .models import  Holdingmutual
from products.models import  Product

# Create your views here.
def addmutual(request):
    mutualfunds= Product.objects
    return render(request,'holdings/addmutual.html',{'mutualfunds':mutualfunds})

def portfolio(request):
    holdings= Holdingmutual.objects.filter(userid_id=request.user.id)
    products= Product.objects
   
    return render(request,'holdings/portfolio.html',{'portfolioList':holdings,'productList':products})