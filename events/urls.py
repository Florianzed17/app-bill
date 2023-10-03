from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/achat/', views.achat, name='achat'),
    path('events/<int:event_id>/achat/confirmation/', views.confirmation, name='confirmation'),
    path('events/search/', views.search_results, name='search'),

]
