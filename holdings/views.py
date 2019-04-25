from django.shortcuts import render,get_object_or_404,redirect
from .models import  Holdingmutual
from products.models import Product
from .forms import MutualForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response 
from dal import autocomplete
#from django.views.generic.edit import CreateView
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from pprint import pprint
import requests

#from django.core.urlresolvers import reverse_lazy






# Create your views here.
def addmutual(request):
    mutualfunds= Product.objects
    return render(request,'holdings/addmutual.html',{'mutualfunds':mutualfunds})

def portfolio(request):
    holdings= Holdingmutual.objects.filter(userid_id=request.user.id)
    #pprint(holdings)
    products= Product.objects
    portfolioList=[]
    for holding in holdings:
        productcode=get_object_or_404(Product,pk=holding.productid_id)
        url = 'https://www.quandl.com/api/v3/datasets/AMFI/'+str(productcode.stockid)+'.json?api_key=a6QtRRy_axhp9mTMRvyC'
        #print(url)
        response=requests.get(url)
        stockdetail=response.json()
        navst=stockdetail['dataset']['data'][0][1]
        #print(navst)
        # Creation of a list with all values required for portfolio
        portfList=[
                   holding.id,
                   productcode.title,
                   holding.no_shares,
                   holding.start_date,
                   holding.sip_date,
                   holding.notes,
                   navst,
                   (navst*holding.no_shares),
                   holding.productid_id,
                   productcode.stockid
                   ]
        portfolioList.append(portfList)
        #pprint(portfolioList)
    return render(request,'holdings/portfolio.html',{'portfolioList':portfolioList,'productList':products})
@login_required
def addmutual2(request):
    if request.method == "POST":
        form = MutualForm(data=request.POST)
        if form.is_valid():
            print("form is valide")
            mutual_form = form.save(commit=False)
            mutual_form.userid_id=request.user.id
            mutual_form.save()
            return redirect('portfolio')
        else:
            print("form is not valide")
            print(request.user)

    else:
        form = MutualForm()
    return render(request, 'holdings/addmutual2.html',{'form':form})
@login_required    
def delmutual(request):
    if request.method == "POST":
        if request.method == 'POST':
            holdid=request.POST['mfund2']
            Holdingmutual.objects.filter(id=holdid).delete()
            print("record deleted"+request.POST['mfund2'])
            return redirect('portfolio')
        return redirect('portfolio')

#example class view- code not used

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

##autocomplete view
class ProductAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Product.objects.none()

        qs = Product.objects.all()

        if self.q:
            qs = qs.filter(title__icontains=self.q)
        
        return qs

class ViewDummyUserCreate4(CreateView):
    # make a form based on this model
    model = Holdingmutual
    # if we only want to edit these two fields
    # fields = ('first_name', 'last_name')
    form_class = MutualForm
    #fields = '__all__'
 
    # render this html file, pass a form object to that file
    template_name = 'holdings/addmutual2.html'
 
    def form_valid(self, form):
        print("form is valide")
        mutual_form2 = form.save(commit=False)
        mutual_form2.submitted_by = self.request.user
        mutual_form2.userid_id=self.request.user.id
        mutual_form2.save()       
        return HttpResponseRedirect(self.get_success_url())
 
    def get_success_url(self):
        return reverse('portfolio')

#Have to implement user based checking
class ViewUpdatePost(UpdateView): 
    model = Holdingmutual
    #form_class = MutualForm
    template_name = 'holdings/editmutual.html'
    fields = ['no_shares','start_date','sip_date','notes']
    #success_url='holdings/portfolios'
    queryset=Holdingmutual.objects.all()
    
 
    def get_object(self):
        #holdid=self.request.POST['mfund2']
        #print("holdid got  ** -"+holdid)
        print("get_object_worked"+self.kwargs['pk'])
        id = self.kwargs['pk']
        return self.model.objects.get(pk=self.kwargs['pk'])
        #return get_object_or_404(Holdingmutual,id=self.kwargs['pk'])
   # def get_initial(self):
   #     return { 'no_shares': 'foo', 'start_date': 'bar','sip_date': 'bar','notes': 'bar' }
 
    def form_valid(self, form):
        print("form is valide")
        mutual_form2 = form.save(commit=False)
        mutual_form2.save()       
        return HttpResponseRedirect(self.get_success_url())
 
    def get_success_url(self):
        return reverse('portfolio')