from django.urls import path
from .views import *

urlpatterns=[
  path('hello/', hello, name='hello'),
  path('listproductsapi/', listproductsapi, name='listproductsapi'),
  path('addapi/', addapi, name='addapi'),
  path('<pk>', productDetailsapi, name='productDetailsapi'),
  path('update/<pk>', update, name='update'),
  path('deleteapi/<id>', deleteapi, name='deleteapi'),
]