from django.shortcuts import render,get_object_or_404
from .models import  Holdingmutual
from products.models import Product
from .forms import MutualForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def addmutual(request):
    mutualfunds= Product.objects
    return render(request,'holdings/addmutual.html',{'mutualfunds':mutualfunds})

def portfolio(request):
    holdings= Holdingmutual.objects.filter(userid_id=request.user.id)
    products= Product.objects
   
    return render(request,'holdings/portfolio.html',{'portfolioList':holdings,'productList':products})
@login_required
def addmutual2(request):
    if request.method == "POST":
        form = MutualForm(data=request.POST)
        if form.is_valid():
            print("form is valide")
            mutual_form = form.save(commit=False)
            mutual_form.userid_id=request.user.id
            mutual_form.save()
        else:
            print("form is not valide")
            print(request.user)

    else:
        form = MutualForm()
    return render(request, 'holdings/addmutual2.html',{'form':form})

