from django.urls import path
from . import views


urlpatterns = [ 
    path('',views.home,name='home'),
    path('view_event/<str:id>/',views.view_event,name='view_event'),
]