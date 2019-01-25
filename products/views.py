from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests
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
    #products=Product.objects
    #
    search_term=''
    funddataList= Product.objects.get_queryset().order_by('stockid')
    if 'search' in request.GET:
        search_term=request.GET['search']
        funddataList= Product.objects.filter(title__icontains=search_term)
        print(*funddataList)

    print("called")
    
    return render(request, 'products/home.html', {
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
    productcode=get_object_or_404(Product,pk=product_id)
    url = 'https://www.quandl.com/api/v3/datasets/AMFI/'+str(productcode.stockid)+'.json?api_key=a6QtRRy_axhp9mTMRvyC'
    print(url)
    response=requests.get(url)
    stockdetail=response.json()
    return render(request,'products/detail.html',{'stockdetail':stockdetail['dataset']})

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



