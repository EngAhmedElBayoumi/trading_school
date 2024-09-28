from . import views
from django.urls import path

app_name = 'landing_page'
urlpatterns = [
    path('', views.LandingPage, name='LandingPage'),
    
    
    path('userlandingpage/', views.UserLandingPagedef, name='UserLandingPage'),
    
    
    # out
    path('page/<str:pagename>', views.outuserlandingpage, name='outuserlandingpage'),
]