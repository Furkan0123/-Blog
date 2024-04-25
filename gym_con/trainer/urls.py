
from django.urls import path
from .import views

urlpatterns = [
   
    path('', views.trainer_list, name= 'trainer'),
    path('<slug:category_slug>/<int:trainer_id>', views.trainer_detail, name= 'trainer_detail'),
    path('categories/<slug:category_slug>', views.category_detail, name= 'trainer_by_category'),
    path('tags/<slug:tag_slug>', views.tag_detail, name= 'trainer_by_tag')
]