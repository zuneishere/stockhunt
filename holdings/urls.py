from django.urls import path
from django.conf.urls import url
import holdings.views
from .views import ProductAutocompleteView
from .views import ViewDummyUserCreate4,ViewDummyUserCreate5,ViewUpdatePost


urlpatterns = [
    #path('',accounts.views.login,name='login'),
    #    path('<int:blogid>/',accounts.views.detail,name='details'),
    #path('addmutual2/',holdings.views.addmutual2,name='addmutual2'),
    path('portfolio/',holdings.views.portfolio,name='portfolio'),
    path('portfolio/delmutual/',holdings.views.delmutual,name='delmutual'),
  #  path('portfolio/<int:pk>/update/',ViewUpdatePost.as_view(), name='editmutual'),
 #   path('editmutual/<int:pk>/',
    url(r'^addmutual/product-autocomplete/$', ProductAutocompleteView.as_view(), name='product-autocomplete'),
    url(r'^addmutual/$', ViewDummyUserCreate4.as_view(), name='addmutual'),
    url(r'^addmutualsip/$', ViewDummyUserCreate5.as_view(), name='addmutualsip'),
    url(r'^update/(?P<pk>\d+)$', ViewUpdatePost.as_view(), name="editmutual"),
    #url(r'^editmutual/<int:pk>/update/$', ViewUpdatePost.as_view(), name='editmutual'),

    
      
]