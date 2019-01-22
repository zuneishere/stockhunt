from django.urls import path
import products.views

urlpatterns = [
    #path('',accounts.views.login,name='login'),
    #    path('<int:blogid>/',accounts.views.detail,name='details'),
    path('create/',products.views.create,name='create'),
    path('<int:product_id>/',products.views.detail,name='detail'),
    
]
