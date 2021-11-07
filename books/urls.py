from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='views.index'),
    path('<int:id>',views.shows,name = 'views.shows')
]
