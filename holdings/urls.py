from django.urls import path
from django.conf.urls import url
import holdings.views
from .views import ProductAutocompleteView
from .views import ViewDummyUserCreate4


urlpatterns = [
    #path('',accounts.views.login,name='login'),
    #    path('<int:blogid>/',accounts.views.detail,name='details'),
    #path('addmutual2/',holdings.views.addmutual2,name='addmutual2'),
    path('portfolio/',holdings.views.portfolio,name='portfolio'),
    path('portfolio/delmutual/',holdings.views.delmutual,name='delmutual'),
    url(r'^addmutual2/product-autocomplete/$', ProductAutocompleteView.as_view(), name='product-autocomplete'),
    url(r'^addmutual2/$', ViewDummyUserCreate4.as_view(), name='addmutual2'),
    
      
]