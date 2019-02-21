from django.urls import path
import products.views
from .views import ChartData

urlpatterns = [
    #path('',accounts.views.login,name='login'),
    #    path('<int:blogid>/',accounts.views.detail,name='details'),
    path('create/',products.views.create,name='create'),
    path('api/chart/data/', ChartData.as_view()),
    path('<int:product_id>/',products.views.detail,name='detail'),
    
    
]
