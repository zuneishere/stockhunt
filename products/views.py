from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework.response import Response
from nsetools import Nse
from pprint import pprint # just for neatness of display
from datetime import datetime, timedelta
import pandas as pd
import io
from bsedata.bse import BSE
import requests
from django import template



defaultfundprice = 0
search_term=''


# Create your views here.




def getPageData(request, allFundList):
    page = request.GET.get('page', 1)
    paginator = Paginator(allFundList, 30)
    print(paginator.count)
    try:
        funds = paginator.page(page)
    except PageNotAnInteger:
        funds = paginator.page(1)
    except EmptyPage:
        funds = paginator.page(paginator.num_pages)
    return funds

def home(request):
   
    nse = Nse()
    top_gainers_nse = nse.get_top_gainers()
    top_losers_nse = nse.get_top_losers()
    bse = BSE()
    top_gainers_bse = bse.topGainers()
    top_losers_bse = bse.topLosers()

    t = datetime.now()
    todate=t.strftime('%Y-%m-%d')
    yesterday = datetime.now() - timedelta(days=1)     
    fromdate=yesterday.strftime('%d/%m/%Y')
    nifty_indice = nse.get_index_quote('NIFTY 50')
    category = "market_cap/broad"
    #bse index using bsetools-not working
    #bse_indice= bse.getIndices(category)
    #pprint(bse_indice)
    #Quandl
    charturl='https://www.quandl.com/api/v3/datasets/NSE/NIFTY_50.json?start_date=2008-01-01&end_date='+todate+'&api_key=a6QtRRy_axhp9mTMRvyC'
    url2='https://www.quandl.com/api/v3/datasets/BSE/SENSEX.json?start_date=2008-01-01&end_date='+todate+'&api_key=a6QtRRy_axhp9mTMRvyC'
    #bseurl='https://api.bseindia.com/BseIndiaAPI/api/ProduceCSVForDate/w?strIndex=SENSEX&dtFromDate='+fromdate+'&dtToDate='+todate
    ##moneycontrol appfeeds
    bseurl='http://appfeeds.moneycontrol.com/jsonapi/market/indices&ind_id=4'
    nseurl='http://appfeeds.moneycontrol.com/jsonapi/market/indices&ind_id=9'
    print(url2)
    #Trying to get csv data from bseindia. You can use these if moneycontrol doesn't work
    # try:
    #     df=pd.read_csv(bseurl)
    #     csvlist=df.iat[1,3]
    # except:
    #     csvlist=0
    
    # print(csvlist)
    response=requests.get(bseurl)
    bsedetail=response.json()
    response=requests.get(nseurl)
    nsedetail=response.json()
    #Chartdetail for different dates
    response3=requests.get(url2)
    chartdetail=response3.json()
    if response3.status_code == 429:
        return render(request,'products/home.html',{
         'bsedetail':bsedetail,
         'nifty':nsedetail,
         'topgainersnse':top_gainers_nse,
         'toplosersnse':top_losers_nse,
         'topgainersbse':top_gainers_bse,
         'toplosersbse':top_losers_bse,
        
         })
    else:
        return render(request,'products/home.html',{
         'bsedetail':bsedetail,
         'nifty':nsedetail,
         'chartdetail':chartdetail['dataset'],
         'chartlist5days':chartdetail['dataset']['data'][:30],
         'topgainersnse':top_gainers_nse,
         'toplosersnse':top_losers_nse,
         'topgainersbse':top_gainers_bse,
         'toplosersbse':top_losers_bse,
        
         })
    
  
    

def mutualfunds(request):
    #products=Product.objects
    #
    search_term=''
    funddataList= Product.objects.get_queryset().order_by('stockid')
    if 'search' in request.GET:
        search_term=request.GET['search']
        funddataList= Product.objects.filter(title__icontains=search_term)
        #print(*funddataList)

    print("called")
    
    return render(request, 'products/mutual.html', {
        'fundList': getPageData(request, funddataList),
        'search': search_term,
    })
    #return render(request,'products/home.html',{'products':products})

@login_required
#Function to create a new stock record if required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['stockid']:
            product=Product()
            product.stockid=request.POST['stockid']
            product.title=request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='http://'+request.POST['url']
            product.icon=request.FILES['icon']
            product.save()
            return redirect('/products/'+str(product.id))


        else:
            return render(request,'products/create.html',{'error':'Fields incomplete!'})

    else:
        return render(request,'products/create.html')
@login_required
def detail(request,product_id):
    nse = Nse()
    top_gainers = nse.get_top_gainers()
    top_losers = nse.get_top_losers()


    productcode=get_object_or_404(Product,pk=product_id)
    url = 'https://www.quandl.com/api/v3/datasets/AMFI/'+str(productcode.stockid)+'.json?api_key=a6QtRRy_axhp9mTMRvyC'
    url2='https://www.quandl.com/api/v3/datasets/BSE/SENSEX.json?api_key=a6QtRRy_axhp9mTMRvyC'

    print(url)
    response=requests.get(url)
    stockdetail=response.json()
    return render(request,'products/detail.html',{'stockdetail':stockdetail['dataset'],'topgainers':top_gainers,'toplosers':top_losers})

def admutual(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://'+request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/'+str(product.id))

        else:
            return render(request, 'products/addmutual.html', {'error': 'Fields incomplete!'})

    else:
        return render(request, 'products/addmutual.html')





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



