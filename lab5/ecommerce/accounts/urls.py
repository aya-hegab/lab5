
from django.urls import path, include
from django.conf.urls.static import static
from .views import *  

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', myProfile,name='myProfile'),
    path('register/', registerationForm.as_view(),name='myRegister'),
]