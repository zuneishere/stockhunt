from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import products.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',products.views.home,name='homepage'),
    path('mutualfunds/',products.views.mutualfunds,name='mutualfunds'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
    path('holdings/',include('holdings.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
