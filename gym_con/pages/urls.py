
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name= 'index'),
    path('why/', views.why, name= 'why'),
    path('contact/', views.contact, name= 'contact'),
    
]