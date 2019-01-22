from django.urls import path
import holdings.views

urlpatterns = [
    #path('',accounts.views.login,name='login'),
    #    path('<int:blogid>/',accounts.views.detail,name='details'),
    path('addmutual/',holdings.views.addmutual,name='addmutual'),
    path('portfolio/',holdings.views.portfolio,name='portfolio'),
      
]