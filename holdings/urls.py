from django.urls import path
import holdings.views


urlpatterns = [
    #path('',accounts.views.login,name='login'),
    #    path('<int:blogid>/',accounts.views.detail,name='details'),
    path('addmutual2/',holdings.views.addmutual2,name='addmutual2'),
    path('portfolio/',holdings.views.portfolio,name='portfolio'),
      
]